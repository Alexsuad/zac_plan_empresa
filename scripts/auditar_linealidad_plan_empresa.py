# File: scripts/auditar_linealidad_plan_empresa.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Auditor determinista de linealidad y extensión.
# Rol: Herramienta de validación técnica (Gate de calidad).
# ──────────────────────────────────────────────────────────────────────

import os
import re
import yaml
import sys
import difflib
from datetime import datetime

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESPUESTAS_DIR = os.path.join(BASE_DIR, "respuestas_plan_empresa")
DOCS_CONTROL_DIR = os.path.join(BASE_DIR, "docs_control")
BUILD_REPORTES_DIR = os.path.join(BASE_DIR, "_build", "reportes")

# Archivos de control
SEDES_YAML = os.path.join(DOCS_CONTROL_DIR, "sedes_informacion_plan_empresa.yml")
LIMITES_YAML = os.path.join(DOCS_CONTROL_DIR, "limites_extension_plan_empresa.yml")

# Secciones a ignorar (coincidencia con compilar_plan_empresa.py)
SECCIONES_IGNORAR = [
    "Datos usados",
    "Pendientes por validar",
    "Notas internas",
    "Anexos relacionados",
    "Conclusión estratégica"
]

def cargar_config():
    if not os.path.exists(SEDES_YAML) or not os.path.exists(LIMITES_YAML):
        print(f"ERROR: Archivos de configuración no encontrados en {DOCS_CONTROL_DIR}")
        sys.exit(1)
    
    with open(SEDES_YAML, 'r', encoding='utf-8') as f:
        sedes = yaml.safe_load(f)
    
    with open(LIMITES_YAML, 'r', encoding='utf-8') as f:
        limites = yaml.safe_load(f)
        
    return sedes, limites

def limpiar_contenido(contenido):
    """Elimina las secciones marcadas para ignorar."""
    lineas = contenido.split('\n')
    lineas_limpias = []
    ignorar = False
    
    for linea in lineas:
        # Detectar inicio de sección a ignorar
        if linea.startswith('##') or linea.startswith('###'):
            ignorar = False
            for seccion in SECCIONES_IGNORAR:
                if seccion.lower() in linea.lower():
                    ignorar = True
                    break
        
        if not ignorar:
            lineas_limpias.append(linea)
            
    return '\n'.join(lineas_limpias)

def obtener_parrafos(contenido):
    """Extrae párrafos significativos (sin tablas, encabezados, etc.)."""
    # Eliminar bloques de código
    contenido = re.sub(r'```.*?```', '', contenido, flags=re.DOTALL)
    
    lineas = contenido.split('\n')
    parrafos = []
    bloque_actual = []
    
    for linea in lineas:
        linea_strip = linea.strip()
        # Ignorar encabezados, tablas, listas cortas y líneas vacías
        if not linea_strip or linea_strip.startswith('#') or '|' in linea_strip or linea_strip.startswith('- ') or linea_strip.startswith('* '):
            if bloque_actual:
                p = ' '.join(bloque_actual)
                if len(p.split()) >= 40: # Solo párrafos de >= 40 palabras
                    parrafos.append(p)
                bloque_actual = []
            continue
        
        bloque_actual.append(linea_strip)
        
    if bloque_actual:
        p = ' '.join(bloque_actual)
        if len(p.split()) >= 40:
            parrafos.append(p)
            
    return parrafos

def auditar():
    sedes_cfg, limites_cfg = cargar_config()
    archivos = sorted([f for f in os.listdir(RESPUESTAS_DIR) if f.endswith('.md')])
    
    reporte_archivos = []
    total_palabras = 0
    parrafos_globales = {} # (texto: archivo)
    similitudes = []
    violaciones_sedes = []
    intros_detectadas = 0
    
    # Ratios
    ratio_p = limites_cfg['ratio_paginas']['principal_palabras_por_pagina']
    ratio_c = limites_cfg['ratio_paginas']['conservador_palabras_por_pagina']

    for archivo in archivos:
        ruta = os.path.join(RESPUESTAS_DIR, archivo)
        with open(ruta, 'r', encoding='utf-8') as f:
            raw_content = f.read()
            
        contenido = limpiar_contenido(raw_content)
        palabras = len(contenido.split())
        total_palabras += palabras
        
        pag_p = round(palabras / ratio_p, 2)
        pag_c = round(palabras / ratio_c, 2)
        
        # Evaluar estado por archivo
        estado_file = "LINEALIDAD_PASS"
        warning_val = limites_cfg['palabras_por_archivo']['apartado_normal_warning']
        fail_val = limites_cfg['palabras_por_archivo']['apartado_normal_fail']
        
        # Aplicar excepciones
        if archivo in limites_cfg.get('excepciones_extension', {}):
            warning_val = limites_cfg['excepciones_extension'][archivo]
            fail_val = warning_val + 500 # Margen proporcional
            
        if palabras > fail_val:
            estado_file = "LINEALIDAD_FAIL"
        elif palabras > warning_val:
            estado_file = "LINEALIDAD_WARNING"
            
        reporte_archivos.append({
            'archivo': archivo,
            'palabras': palabras,
            'pag_p': pag_p,
            'pag_c': pag_c,
            'estado': estado_file
        })
        
        # Buscar intros repetidas
        if re.search(r"Sistreg es", contenido, re.IGNORECASE):
            intros_detectadas += 1
            
        # Análisis de sedes
        for concepto in sedes_cfg['conceptos']:
            for termino in concepto['terminos']:
                if re.search(r'\b' + re.escape(termino) + r'\b', contenido, re.IGNORECASE):
                    # Si no es sede principal ni secundaria
                    sedes_validas = [concepto['sede_principal']] + concepto.get('sedes_secundarias', [])
                    if archivo not in sedes_validas:
                        violaciones_sedes.append({
                            'archivo': archivo,
                            'concepto': concepto['id'],
                            'termino': termino,
                            'sede_esperada': concepto['sede_principal']
                        })
                        break
        
        # Detección de duplicados
        parrafos = obtener_parrafos(contenido)
        for p in parrafos:
            # Comparar con párrafos ya vistos
            for p_visto, arc_visto in parrafos_globales.items():
                if arc_visto == archivo: continue
                
                ratio = difflib.SequenceMatcher(None, p, p_visto).ratio()
                if ratio >= limites_cfg['similitud_parrafos']['warning_min']:
                    similitudes.append({
                        'ratio': round(ratio, 2),
                        'arc1': arc_visto,
                        'arc2': archivo,
                        'snippet': p[:100] + "..."
                    })
            
            parrafos_globales[p] = archivo

    # Totales globales
    total_pag_p = round(total_palabras / ratio_p, 1)
    total_pag_c = round(total_palabras / ratio_c, 1)
    
    # Determinar estado global
    estado_global = "LINEALIDAD_PASS"
    log = []
    
    # 1. Fallos por archivo individual
    archivos_fail = [item['archivo'] for item in reporte_archivos if item['estado'] == "LINEALIDAD_FAIL"]
    if archivos_fail:
        estado_global = "LINEALIDAD_FAIL"
        log.append(f"Falla: Apartados exceden el límite crítico: {', '.join(archivos_fail)}")

    # 2. Similitud crítica
    similitudes_criticas = [s for s in similitudes if s['ratio'] >= limites_cfg['similitud_parrafos'].get('fail_min', 0.88)]
    if similitudes_criticas:
        estado_global = "LINEALIDAD_FAIL"
        log.append(f"Falla: Detectada similitud crítica (>= {limites_cfg['similitud_parrafos'].get('fail_min', 0.88)}) entre {len(similitudes_criticas)} pares de archivos.")

    # 3. Violaciones de sede con severidad FAIL
    violaciones_fail = []
    for v in violaciones_sedes:
        concepto_id = v['concepto']
        config_concepto = next((c for c in sedes_cfg['conceptos'] if c['id'] == concepto_id), None)
        if config_concepto and config_concepto.get('severidad_si_excede') == "LINEALIDAD_FAIL":
            violaciones_fail.append(v)
    
    if violaciones_fail:
        estado_global = "LINEALIDAD_FAIL"
        log.append(f"Falla: Violación crítica de sedes de información en {len(violaciones_fail)} conceptos.")

    # 4. Regla de páginas (Límite Global)
    lim = limites_cfg['limites_globales']
    if total_pag_p > lim['fail_mas_de_paginas']:
        estado_global = "LINEALIDAD_FAIL"
        log.append(f"Falla: Extensión total ({total_pag_p} pág) excede límite crítico ({lim['fail_mas_de_paginas']} pág).")
    elif total_pag_p > lim['warning_leve_hasta_paginas'] and estado_global == "LINEALIDAD_PASS":
        estado_global = "LINEALIDAD_WARNING"
        log.append(f"Aviso: Extensión total ({total_pag_p} pág) en zona de riesgo.")
        
    # 5. Regla de intros repetidas
    if intros_detectadas > limites_cfg['intros_definitorias']['max_permitidas']:
        estado_global = "LINEALIDAD_FAIL"
        log.append(f"Falla: Demasiadas introducciones definitorias ({intros_detectadas}/{limites_cfg['intros_definitorias']['max_permitidas']}).")

    # Generar Reporte Markdown
    if not os.path.exists(BUILD_REPORTES_DIR):
        os.makedirs(BUILD_REPORTES_DIR)
        
    reporte_path = os.path.join(BUILD_REPORTES_DIR, "auditoria_linealidad_plan_empresa.md")
    
    with open(reporte_path, 'w', encoding='utf-8') as r:
        r.write(f"# Reporte de Auditoría de Linealidad Documental\n\n")
        r.write(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        r.write(f"**Estado Global:** `{estado_global}`\n\n")
        
        r.write(f"## 1. Resumen de Extensión\n")
        r.write(f"- **Palabras Totales:** {total_palabras}\n")
        r.write(f"- **Páginas Estimadas (Ratio Principal 300):** **{total_pag_p}**\n")
        r.write(f"- **Páginas Estimadas (Ratio Conservador 250):** {total_pag_c}\n\n")
        
        r.write(f"## 2. Detalle por Archivo\n")
        r.write(f"| Archivo | Palabras | Pág (300) | Pág (250) | Estado |\n")
        r.write(f"|---|---|---|---|---|\n")
        for item in reporte_archivos:
            r.write(f"| {item['archivo']} | {item['palabras']} | {item['pag_p']} | {item['pag_c']} | `{item['estado']}` |\n")
        
        if violaciones_sedes:
            r.write(f"\n## 3. Conceptos Fuera de Sede\n")
            r.write(f"| Archivo | Concepto | Término detectado | Sede Principal |\n")
            r.write(f"|---|---|---|---|\n")
            for v in violaciones_sedes[:15]:
                r.write(f"| {v['archivo']} | {v['concepto']} | {v['termino']} | {v['sede_esperada']} |\n")
                
        if similitudes:
            r.write(f"\n## 4. Párrafos Similares Detectados (Repetición)\n")
            r.write(f"| Ratio | Archivo A | Archivo B | Fragmento |\n")
            r.write(f"|---|---|---|---|\n")
            # Ordenar por ratio descendente
            similitudes.sort(key=lambda x: x['ratio'], reverse=True)
            for s in similitudes[:10]:
                r.write(f"| {s['ratio']} | {s['arc1']} | {s['arc2']} | {s['snippet']} |\n")

        if log:
            r.write(f"\n## 5. Hallazgos Críticos\n")
            for l in log:
                r.write(f"- {l}\n")
                
    print(f"Reporte generado en: {reporte_path}")
    print(f"Estado Global: {estado_global}")
    
    # Política de Exit Codes: FAIL=1, WARNING/PASS=0
    if estado_global == "LINEALIDAD_FAIL":
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    auditar()
