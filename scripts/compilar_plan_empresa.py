import os
import re
import sys
import shutil
import subprocess

try:
    import yaml
except ImportError:
    print("FAIL: El paquete 'pyyaml' no está instalado. Instala las dependencias con: pip install -r requirements.txt")
    sys.exit(1)

def check_linearity_gate(is_test_mode):
    """Verifica si el reporte de linealidad permite continuar."""
    reporte_path = '_build/reportes/auditoria_linealidad_plan_empresa.md'
    
    if not os.path.exists(reporte_path):
        msg = "FAIL: No existe el reporte de linealidad. Ejecuta scripts/auditar_linealidad_plan_empresa.py primero."
        print(msg)
        if not is_test_mode:
            sys.exit(1)
        return
        
    with open(reporte_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "LINEALIDAD_FAIL" in content:
        if not is_test_mode:
            print("FAIL: El plan ha fallado la auditoría de linealidad.")
            sys.exit(1)
        else:
            print("WARNING: El plan ha fallado la auditoría de linealidad (Ignorado en modo test).")
    elif "LINEALIDAD_WARNING" in content:
        if not is_test_mode:
            print("FAIL: Entrega bloqueada por LINEALIDAD_WARNING. Revisa el reporte.")
            sys.exit(1)
        else:
            print("WARNING: El plan tiene avisos de linealidad documental (Continuando en modo test).")
    elif "LINEALIDAD_PASS" in content:
        print("PASS: Auditoría de linealidad superada.")
    else:
        if not is_test_mode:
            print("FAIL: Estado de linealidad no reconocido en el reporte.")
            sys.exit(1)
        else:
            print("WARNING: Estado de linealidad no reconocido en el reporte (Ignorado en modo test).")


def read_manifest(manifest_path):
    if not os.path.exists(manifest_path):
        return []
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        if not data:
            return []
        anexos_list = data.get('anexos')
        return anexos_list if anexos_list is not None else []

def strip_internal_notes(content):
    patrones_excluir = [
        r'(?i)datos usados', 
        r'(?i)pendientes por validar', 
        r'(?i)notas internas',
        r'(?i)anexos relacionados',
        r'(?i)conclusión estratégica'
    ]
    
    lineas = content.split('\n')
    lineas_filtradas = []
    ignorar_nivel = 0
    
    for linea in lineas:
        match_titulo = re.match(r'^(#{1,6})\s+(.*)', linea)
        if match_titulo:
            nivel = len(match_titulo.group(1))
            titulo = match_titulo.group(2)
            
            if ignorar_nivel > 0:
                if nivel <= ignorar_nivel:
                    ignorar_nivel = 0
                else:
                    continue
            
            if ignorar_nivel == 0:
                for pat in patrones_excluir:
                    if re.search(pat, titulo):
                        ignorar_nivel = nivel
                        break
                        
            if ignorar_nivel > 0:
                continue
                
        if ignorar_nivel == 0:
            lineas_filtradas.append(linea)
            
    return '\n'.join(lineas_filtradas)

def compile_plan():
    is_test_mode = '--test' in sys.argv

    respuestas_dir = 'respuestas_plan_empresa/'
    build_dir = '_build/test/' if is_test_mode else '_build/'
    anexos_entrega_dir = os.path.join(build_dir, 'entrega', 'anexos')
    reportes_dir = os.path.join(build_dir, 'reportes')
    manifest_path = 'anexos/manifest_anexos.yml'
    
    build_md = os.path.join(build_dir, 'plan_empresa_sistreg_completo.md')
    report_file = os.path.join(reportes_dir, 'manifest_compilacion.md')
    
    obligatorios_prefixes = [
        '01_', '02_', '03_1_', '03_2_', '03_3_', '04_', '05_', 
        '06_0_', '06_1_', '06_2_', '06_3_', '06_4_', '06_5_', '07_', '08_'
    ]
    
    files = sorted([f for f in os.listdir(respuestas_dir) if f.endswith('.md')])
    
    if '00_indice_respuestas_plan_empresa.md' in files:
        files.remove('00_indice_respuestas_plan_empresa.md')
        
    faltantes = []
    for prefix in obligatorios_prefixes:
        if not any(f.startswith(prefix) for f in files):
            faltantes.append(prefix)

    if faltantes:
        if not is_test_mode:
            print(f"FAIL: Faltan apartados obligatorios: {faltantes}")
            sys.exit(1)
        else:
            print(f"WARNING: Faltan apartados obligatorios: {faltantes} (Ignorado en modo test).")
    
    # Gate de Linealidad Documental
    check_linearity_gate(is_test_mode)
        
    block_patterns = [r'Pendiente de completar', r'\[PENDIENTE\]', r'\[CIFRA\]', r'\[NÚMERO\]']
    
    print("Iniciando validación y compilación de archivos...")
    
    incluidos = []
    advertencias = []
    bloqueos = []
    
    final_content = "# Plan de Empresa - Sistreg\n\n"
    
    for f in files:
        filepath = os.path.join(respuestas_dir, f)
        with open(filepath, 'r', encoding='utf-8') as infile:
            content = infile.read()
            
            for pat in block_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    bloqueos.append(f"Archivo {f} contiene marcador de bloqueo: {pat}")
                    
            content_limpio = strip_internal_notes(content)
            
            final_content += f"<!-- Source: {f} -->\n"
            final_content += content_limpio
            final_content += "\n\n---\n\n"
            incluidos.append(f)
            
    anexos_internos = []
    anexos_externos = []
    anexos_a_copiar = []
    anexos = read_manifest(manifest_path)
    
    anexos_validos = []
    for ax in anexos:
        ruta = ax.get('ruta')
        if not os.path.exists(ruta):
            bloqueos.append(f"Anexo {ax.get('id')} declarado pero no encontrado en: {ruta}")
            continue
        anexos_validos.append(ax)
        
    if bloqueos:
        if not is_test_mode:
            for b in bloqueos:
                print(f"FAIL: {b}")
            os.makedirs(reportes_dir, exist_ok=True)
            with open(report_file, 'w', encoding='utf-8') as rf:
                rf.write("# Reporte de Compilación Fallida\n\n")
                for b in bloqueos:
                    rf.write(f"- {b}\n")
            print("Compilación bloqueada por marcadores o anexos pendientes.")
            sys.exit(1)
        else:
            for b in bloqueos:
                print(f"WARNING: {b} (Ignorado en modo test)")
            print("INFO: Modo prueba activo. Continuando a pesar de marcadores o anexos pendientes.")
        
    if anexos_validos:
        final_content += "# Anexos\n\n"
        
        for ax in anexos_validos:
            if ax.get('incluir_en_documento'):
                final_content += f"## {ax.get('id')} - {ax.get('titulo')}\n\n"
                ruta = ax.get('ruta')
                tipo = ax.get('tipo', 'markdown').lower()
                
                if tipo == 'markdown':
                    with open(ruta, 'r', encoding='utf-8') as f_ax:
                        final_content += f_ax.read() + "\n\n"
                elif tipo in ['imagen', 'grafico', 'grafica', 'image', 'png', 'jpg']:
                    final_content += f"![{ax.get('titulo')}]({ruta})\n\n"
                else:
                    advertencias.append(f"Tipo interno no soportado para incrustar: {tipo} ({ax.get('id')})")
                    
                anexos_internos.append(ax.get('id'))
            else:
                anexos_externos.append(ax)

        if anexos_externos:
            final_content += "## Documentación Externa Adjunta\n\n"
            final_content += "| ID | Título | Tipo | Descripción | Archivo |\n"
            final_content += "|---|---|---|---|---|\n"
            for ax in anexos_externos:
                ruta_orig = ax.get('ruta')
                nombre_archivo = os.path.basename(ruta_orig)
                ruta_dest = os.path.join(anexos_entrega_dir, nombre_archivo)
                anexos_a_copiar.append((ruta_orig, ruta_dest))
                
                desc = ax.get('descripcion', '')
                tipo = ax.get('tipo', 'documento')
                final_content += f"| {ax.get('id')} | {ax.get('titulo')} | {tipo} | {desc} | `{nombre_archivo}` |\n"
    
    # SALIDA ATÓMICA: Todo se genera y guarda si no hay bloqueos (o ignoramos por test_mode)
    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(anexos_entrega_dir, exist_ok=True)
    os.makedirs(reportes_dir, exist_ok=True)
    
    for origen, destino in anexos_a_copiar:
        shutil.copy2(origen, destino)

    # Registro de resultados
    format_results = {
        "MARKDOWN": "PENDING",
        "DOCX": "PENDING",
        "PDF": "PENDING"
    }

    try:
        with open(build_md, 'w', encoding='utf-8') as outfile:
            outfile.write(final_content)
        format_results["MARKDOWN"] = "PASS"
        print(f"MARKDOWN_PASS: Consolidado en {build_md}")
    except Exception as e:
        format_results["MARKDOWN"] = "FAIL"
        print(f"MARKDOWN_FAIL: Error escribiendo MD: {e}")
        sys.exit(1)
        
    build_docx = os.path.join(build_dir, 'plan_empresa_sistreg_completo.docx')
    ref_docx = 'docs_base/plantillas/reference.docx'
    
    try:
        cmd_pandoc = ['pandoc', '-f', 'markdown-yaml_metadata_block', build_md, '-o', build_docx]
        if os.path.exists(ref_docx):
            cmd_pandoc.extend(['--reference-doc', ref_docx])
        else:
            advertencias.append("Plantilla docs_base/plantillas/reference.docx no existe. Se usó estilo por defecto.")
            print("INFO: Plantilla reference.docx no encontrada. Generando con estilos por defecto.")
            
        result = subprocess.run(cmd_pandoc, capture_output=True, text=True)
        if result.returncode != 0:
            format_results["DOCX"] = "FAIL"
            print(f"DOCX_FAIL: Pandoc falló: {result.stderr}")
        else:
            format_results["DOCX"] = "PASS"
            print(f"DOCX_PASS: Generado en {build_docx}")
            
            # Intentar generar PDF si DOCX tuvo éxito
            try:
                cmd_pdf = ['libreoffice', '--headless', '--convert-to', 'pdf', build_docx, '--outdir', build_dir]
                res_pdf = subprocess.run(cmd_pdf, capture_output=True, text=True)
                if res_pdf.returncode == 0:
                    format_results["PDF"] = "PASS"
                    print(f"PDF_PASS: Generado en {build_dir}")
                else:
                    format_results["PDF"] = "FAIL"
                    print(f"PDF_FAIL: LibreOffice falló: {res_pdf.stderr}")
            except FileNotFoundError:
                format_results["PDF"] = "SKIPPED"
                print("PDF_SKIPPED: libreoffice no está disponible.")
            
    except FileNotFoundError:
        format_results["DOCX"] = "FAIL"
        format_results["PDF"] = "SKIPPED"
        print("DOCX_FAIL: pandoc no está disponible.")
        
    # Generar reporte final
    with open(report_file, 'w', encoding='utf-8') as rf:
        rf.write("# Reporte de Compilación\n\n")
        rf.write(f"**Estado General:** {'PASS' if all(v in ['PASS', 'SKIPPED'] for v in format_results.values()) else 'FAIL'}\n\n")
        rf.write("## Resultados por Formato\n")
        for fmt, res in format_results.items():
            rf.write(f"- {fmt}: {res}\n")
            
        rf.write("\n## Apartados incluidos\n")
        for f in incluidos:
            rf.write(f"- {f}\n")
            
        rf.write("\n## Anexos insertados (Internos)\n")
        for ax in anexos_internos:
            rf.write(f"- {ax}\n")
            
        rf.write("\n## Anexos referenciados (Externos)\n")
        for ax in anexos_externos:
            rf.write(f"- {ax.get('id')} ({ax.get('ruta')})\n")
            
        rf.write("\n## Advertencias\n")
        if advertencias:
            for adv in advertencias:
                rf.write(f"- {adv}\n")
        else:
            rf.write("- Ninguna\n")

    # Resumen final en consola
    print("-" * 30)
    print("RESUMEN DE COMPILACIÓN:")
    for fmt, res in format_results.items():
        print(f"  {fmt}: {res}")
    print("-" * 30)

    # Lógica de salida determinista
    if is_test_mode:
        print("INFO: Modo prueba activo. El script termina con EXIT 0 a pesar de posibles fallos en DOCX/PDF.")
        sys.exit(0)
    else:
        if any(v == "FAIL" for v in format_results.values()):
            print("FAIL: La compilación ha fallado en uno o más formatos obligatorios.")
            sys.exit(1)
        print("PASS: Compilación finalizada exitosamente.")
        sys.exit(0)

if __name__ == '__main__':
    compile_plan()
