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
        print(f"FAIL: Faltan apartados obligatorios: {faltantes}")
        if not is_test_mode:
            sys.exit(1)
        else:
            print("INFO: Modo prueba activo. Ignorando error de apartados faltantes.")
        
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
        for b in bloqueos:
            print(f"FAIL: {b}")
            
        os.makedirs(reportes_dir, exist_ok=True)
        with open(report_file, 'w', encoding='utf-8') as rf:
            rf.write("# Reporte de Compilación Fallida\n\n")
            for b in bloqueos:
                rf.write(f"- {b}\n")
        print("Compilación bloqueada por marcadores o anexos pendientes.")
        
        if not is_test_mode:
            sys.exit(1)
        else:
            print("INFO: Modo prueba activo. Ignorando error de marcadores y anexos.")
        
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

    with open(build_md, 'w', encoding='utf-8') as outfile:
        outfile.write(final_content)
        
    print(f"Markdown consolidado en: {build_md}")
    
    build_docx = os.path.join(build_dir, 'plan_empresa_sistreg_completo.docx')
    ref_docx = 'docs_base/plantillas/reference.docx'
    
    try:
        cmd_pandoc = ['pandoc', build_md, '-o', build_docx]
        if os.path.exists(ref_docx):
            cmd_pandoc.extend(['--reference-doc', ref_docx])
        else:
            advertencias.append("Plantilla docs_base/plantillas/reference.docx no existe. Se usó estilo por defecto.")
            print("INFO: Plantilla reference.docx no encontrada. Generando con estilos por defecto.")
            
        result = subprocess.run(cmd_pandoc, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"FAIL: Pandoc falló: {result.stderr}")
            if not is_test_mode:
                sys.exit(1)
        else:
            print(f"DOCX generado en: {build_docx}")
            
            try:
                cmd_pdf = ['libreoffice', '--headless', '--convert-to', 'pdf', build_docx, '--outdir', build_dir]
                res_pdf = subprocess.run(cmd_pdf, capture_output=True, text=True)
                if res_pdf.returncode == 0:
                    print(f"PDF generado exitosamente en {build_dir}")
                else:
                    print(f"WARNING: LibreOffice falló al generar PDF: {res_pdf.stderr}")
            except FileNotFoundError:
                print("WARNING: libreoffice no está disponible. No se generó el PDF.")
            
    except FileNotFoundError:
        print("WARNING: pandoc no está disponible. No se generaron DOCX/PDF.")
        
    with open(report_file, 'w', encoding='utf-8') as rf:
        rf.write("# Reporte de Compilación\n\n")
        rf.write("## Apartados incluidos\n")
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
            
    print("PASS: Compilación finalizada correctamente.")

if __name__ == '__main__':
    compile_plan()
