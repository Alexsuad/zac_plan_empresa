# File: scripts/auditar_lexico_comunicacion.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Auditor léxico de identidad verbal Sistreg.
# Rol: Herramienta de validación técnica (Gate de calidad).
# ──────────────────────────────────────────────────────────────────────

import os
import re
import yaml
import sys
from datetime import datetime

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESPUESTAS_DIR = os.path.join(BASE_DIR, "respuestas_plan_empresa")
DOCS_CONTROL_DIR = os.path.join(BASE_DIR, "docs_control")
BUILD_REPORTES_DIR = os.path.join(BASE_DIR, "_build", "reportes")

# Archivo de configuración
CONFIG_YAML = os.path.join(DOCS_CONTROL_DIR, "lexico_comunicacion_sistreg.yml")

def cargar_config():
    if not os.path.exists(CONFIG_YAML):
        print(f"ERROR: Archivo de configuración no encontrado en {CONFIG_YAML}")
        sys.exit(1)
    with open(CONFIG_YAML, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def auditar():
    config = cargar_config()
    archivos = sorted([f for f in os.listdir(RESPUESTAS_DIR) if f.endswith('.md')])
    
    cat = config['categorias']
    comerciales = config['configuracion']['capitulos_comerciales']
    
    reporte_global = {
        'estado': 'LEXICO_PASS',
        'hallazgos': [],
        'archivos': []
    }

    for archivo in archivos:
        ruta = os.path.join(RESPUESTAS_DIR, archivo)
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        estado_archivo = 'LEXICO_PASS'
        motivos_archivo = []
        
        # 1. Auditoría de Léxico Logístico Profundo
        logistica_terms = cat['logistica_profunda']['terminos']
        detectados_logistica = []
        for t in logistica_terms:
            matches = re.findall(r'\b' + re.escape(t) + r'\b', contenido, re.IGNORECASE)
            if matches:
                detectados_logistica.append((t, len(matches)))
        
        conteo_logistica = sum(m[1] for m in detectados_logistica)
        min_rec = cat['logistica_profunda']['min_recomendado'].get(archivo, 0)
        
        if conteo_logistica < min_rec:
            # Solo WARNING si no llega al mínimo
            if estado_archivo == 'LEXICO_PASS': estado_archivo = 'LEXICO_WARNING'
            motivos_archivo.append(f"Densidad logística baja ({conteo_logistica}/{min_rec} términos).")

        # 2. Tecnicismos Prohibidos
        tech_terms = cat['tecnicismos_prohibidos']['terminos']
        es_comercial = archivo in comerciales
        
        for t in tech_terms:
            matches = re.findall(r'\b' + re.escape(t) + r'\b', contenido, re.IGNORECASE)
            if matches:
                sev = cat['tecnicismos_prohibidos']['severidad_comercial'] if es_comercial else cat['tecnicismos_prohibidos']['severidad_otros']
                motivos_archivo.append(f"Detectado tecnicismo '{t}' ({len(matches)} veces) -> {sev}")
                if sev == 'LEXICO_FAIL':
                    estado_archivo = 'LEXICO_FAIL'
                elif sev == 'LEXICO_WARNING' and estado_archivo == 'LEXICO_PASS':
                    estado_archivo = 'LEXICO_WARNING'

        # 3. Promesas Peligrosas
        promesa_terms = cat['promesas_peligrosas']['terminos']
        for t in promesa_terms:
            # Búsqueda literal para frases
            if t.lower() in contenido.lower():
                estado_archivo = 'LEXICO_FAIL'
                motivos_archivo.append(f"Detectada promesa peligrosa: '{t}' -> LEXICO_FAIL")

        # 4. Frases Genéricas sin Contexto
        generic_terms = cat['frases_genericas']['terminos']
        # Dividir por párrafos para buscar contexto
        parrafos = [p for p in contenido.split('\n\n') if p.strip()]
        for p in parrafos:
            for t in generic_terms:
                if t.lower() in p.lower():
                    # Buscar si hay algún término logístico en el mismo párrafo
                    tiene_contexto = any(lt.lower() in p.lower() for lt in logistica_terms)
                    if not tiene_contexto:
                        if estado_archivo == 'LEXICO_PASS': estado_archivo = 'LEXICO_WARNING'
                        motivos_archivo.append(f"Frase genérica '{t}' sin contexto logístico en párrafo.")

        # Actualizar estado global
        if estado_archivo == 'LEXICO_FAIL':
            reporte_global['estado'] = 'LEXICO_FAIL'
        elif estado_archivo == 'LEXICO_WARNING' and reporte_global['estado'] == 'LEXICO_PASS':
            reporte_global['estado'] = 'LEXICO_WARNING'
            
        reporte_global['archivos'].append({
            'archivo': archivo,
            'estado': estado_archivo,
            'motivos': motivos_archivo,
            'conteo_logistica': conteo_logistica,
            'detectados_logistica': detectados_logistica[:5] # Top 5
        })

    # Generar Reporte Markdown
    if not os.path.exists(BUILD_REPORTES_DIR):
        os.makedirs(BUILD_REPORTES_DIR)
        
    reporte_path = os.path.join(BUILD_REPORTES_DIR, "auditoria_lexico_sistreg.md")
    
    with open(reporte_path, 'w', encoding='utf-8') as r:
        r.write(f"# Reporte de Auditoría Léxica Sistreg\n\n")
        r.write(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        r.write(f"**Estado Global:** `{reporte_global['estado']}`\n\n")
        
        r.write(f"## 1. Resumen por Archivo\n")
        r.write(f"| Archivo | Estado | Palabras Log. | Detalle |\n")
        r.write(f"|---|---|---|---|\n")
        for arc in reporte_global['archivos']:
            motivos_str = "; ".join(arc['motivos']) if arc['motivos'] else "Correcto"
            r.write(f"| {arc['archivo']} | `{arc['estado']}` | {arc['conteo_logistica']} | {motivos_str} |\n")
            
        r.write(f"\n## 2. Términos de Valor Logístico Detectados (Muestra)\n")
        for arc in reporte_global['archivos']:
            if arc['detectados_logistica']:
                terms_str = ", ".join([f"{t} ({c})" for t, c in arc['detectados_logistica']])
                r.write(f"- **{arc['archivo']}:** {terms_str}\n")

        r.write(f"\n## 3. Criterios Aplicados\n")
        r.write(f"- `LEXICO_FAIL`: Promesas peligrosas o tecnicismos en capítulos comerciales.\n")
        r.write(f"- `LEXICO_WARNING`: Falta de léxico logístico, frases genéricas sin contexto o tecnicismos en capítulos operativos.\n")
        r.write(f"- `LEXICO_PASS`: Identidad verbal alineada con Sistreg (Servicio B2B Logístico).\n")

    print(f"Reporte generado en: {reporte_path}")
    print(f"Estado Global: {reporte_global['estado']}")
    
    # Política de Exit Codes
    if reporte_global['estado'] == "LEXICO_FAIL":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    auditar()
