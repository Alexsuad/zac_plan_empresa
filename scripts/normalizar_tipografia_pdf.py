# File: scripts/normalizar_tipografia_pdf.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Normalizar tipografía, guiones y términos técnicos para el PDF.
# Rol: Limpieza estética final de fuentes Markdown.
# ──────────────────────────────────────────────────────────────────────
import os
import re

def normalizar_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read()

    original = contenido

    # 1. Normalizar notas internas de Git (shorthands)
    contenido = contenido.replace("> [!NOTE]", "**Nota:**")
    contenido = contenido.replace("> [!IMPORTANT]", "**Nota importante:**")
    contenido = contenido.replace("[!NOTE]", "**Nota:**")
    contenido = contenido.replace("[!IMPORTANT]", "**Nota importante:**")

    # 2. Corregir términos partidos (safeguard)
    # Buscamos variantes con espacios o caracteres invisibles
    contenido = re.sub(r'N\s+ot\s+a', 'Nota', contenido)
    contenido = re.sub(r'ej\s+ec\s+uc\s+i\s*ó\s*n', 'ejecución', contenido)
    
    # 3. Normalizar términos técnicos
    # Aseguramos guion estándar y eliminamos variantes raras
    contenido = re.sub(r'e[‐–—]CMR', 'CMR electrónico', contenido)
    contenido = re.sub(r'e[‐–—]FTI', 'eFTI', contenido)
    contenido = contenido.replace('e-FTI', 'eFTI') # Estandarizamos a eFTI sin guion

    # 4. Normalizar guiones largos y especiales
    # Sustituimos rayas em (—) y en (–) por guion normal con espacios para compatibilidad PDF
    contenido = contenido.replace(' — ', ' - ')
    contenido = contenido.replace('—', ' - ')
    contenido = contenido.replace(' – ', ' - ')
    contenido = contenido.replace('–', ' - ')
    contenido = contenido.replace('‐', '-') # Hyphen unicode raro a estándar

    # 5. Limpieza de caracteres invisibles y espacios raros
    contenido = contenido.replace('\u00A0', ' ') # No-break space
    contenido = contenido.replace('\u202F', ' ') # Narrow no-break space
    contenido = contenido.replace('\u200B', '')  # Zero width space

    # 6. Normalizar saltos de línea y espacios dobles accidentales
    contenido = re.sub(r' +', ' ', contenido)
    
    if contenido != original:
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return True
    return False

def main():
    directorio = 'respuestas_plan_empresa'
    archivos_procesados = 0
    archivos_modificados = 0

    for archivo in os.listdir(directorio):
        if archivo.endswith('.md'):
            ruta = os.path.join(directorio, archivo)
            archivos_procesados += 1
            if normalizar_archivo(ruta):
                archivos_modificados += 1
                print(f"Modificado: {archivo}")

    print(f"\nResumen: {archivos_procesados} procesados, {archivos_modificados} modificados.")

if __name__ == "__main__":
    main()
