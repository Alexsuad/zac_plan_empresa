# File: scripts/limpiar_caracteres_pdf.py
from pathlib import Path
import re

CARPETA_FUENTES = Path("respuestas_plan_empresa")

# Diccionario de limpieza de caracteres invisibles o problemáticos
REEMPLAZOS = {
    "\uFFFE": "-",  # Carácter que suele romper guiones en el PDF
    "\uFEFF": "",   # Byte Order Mark
    "\uFFFC": "",   # Object Replacement Character
    "\uFFFD": "",   # Replacement Character
    "\u00AD": "",   # Soft Hyphen
    "\u200B": "",   # Zero Width Space
    "\u200C": "",   # Zero Width Non-Joiner
    "\u200D": "",   # Zero Width Joiner
    "\u2060": "",   # Word Joiner
    "\u2010": "-",  # Hyphen
    "\u2011": "-",  # Non-breaking Hyphen
    "\u2012": "-",  # Figure Dash
    "\u2013": "-",  # En Dash
    "\u2014": "-",  # Em Dash
    "\u2015": "-",  # Horizontal Bar
    "\u2043": "-",  # Hyphen Bullet
    "\u00A0": " ",  # No-break Space
    "\u202F": " ",  # Narrow No-break Space
}

# Normalizaciones explícitas para términos críticos
# Se incluyen variantes con y sin caracteres invisibles detectados
NORMALIZACIONES = [
    # CMR electrónico
    (r"\be\s*[-‐‒–—]?\s*CMRs", "CMRs"),
    (r"\be\s*[-‐‒–—]?\s*CMR", "CMR electrónico"),
    (r"\be\s*[\ufffe\ufeff\ufffc\ufffd\u200b\u200c\u200d\u2060]\s*CMR", "CMR electrónico"),
    
    # dCMRs -> de CMRs
    (r"dCMRs", "de CMRs"),
    (r"deCMRs", "de CMRs"),
    
    # eFTI (sin guion)
    (r"e\s*[-‐‒–—]?\s*FTI", "eFTI"),
    (r"e\s*[\ufffe\ufeff\ufffc\ufffd\u200b\u200c\u200d\u2060]\s*FTI", "eFTI"),
    
    # Económico financiero (sin guion, minúscula)
    (r"Económico\s*[-‐‒–—]?\s*Financiero", "Económico financiero"),
    (r"Económico\s*[\ufffe\ufeff\ufffc\ufffd\u200b\u200c\u200d\u2060]\s*Financiero", "Económico financiero"),
    (r"EconómicoFinanciero", "Económico financiero"),
    
    # documental y económico (con 'y')
    (r"documental\s*[-‐‒–—]?\s*económico", "documental y económico"),
    (r"documental\s*[\ufffe\ufeff\ufffc\ufffd\u200b\u200c\u200d\u2060]\s*económico", "documental y económico"),
    (r"documentaleconómico", "documental y económico"),
    
    # operativo y económica (con 'y')
    (r"operativo\s*[-‐‒–—]?\s*económica", "operativo y económica"),
    (r"operativo\s*[\ufffe\ufeff\ufffc\ufffd\u200b\u200c\u200d\u2060]\s*económica", "operativo y económica"),
    (r"operativoeconómica", "operativo y económica"),
]

def Procesar_Archivo(Ruta_Archivo: Path) -> int:
    """Limpia caracteres problemáticos y normaliza términos en un archivo Markdown."""
    Texto_Original = Ruta_Archivo.read_text(encoding="utf-8")
    Texto_Nuevo = Texto_Original
    Cambios = 0

    # 1. Aplicar reemplazos directos de caracteres
    for Caracter, Reemplazo in REEMPLAZOS.items():
        Cantidad = Texto_Nuevo.count(Caracter)
        if Cantidad:
            Cambios += Cantidad
            Texto_Nuevo = Texto_Nuevo.replace(Caracter, Reemplazo)

    # 2. Aplicar normalizaciones con regex para atrapar espacios o caracteres invisibles
    for Patron, Reemplazo in NORMALIZACIONES:
        # Contamos cuántas veces cambia el texto
        Nuevas_Coincidencias = len(re.findall(Patron, Texto_Nuevo))
        if Nuevas_Coincidencias:
            Nuevo_Texto_Temp = re.sub(Patron, Reemplazo, Texto_Nuevo)
            if Nuevo_Texto_Temp != Texto_Nuevo:
                # Solo contamos cambios reales que alteren el contenido
                Cambios += Nuevas_Coincidencias
                Texto_Nuevo = Nuevo_Texto_Temp

    if Texto_Nuevo != Texto_Original:
        Ruta_Archivo.write_text(Texto_Nuevo, encoding="utf-8")

    return Cambios

def Main() -> int:
    """Ejecuta la limpieza en todas las fuentes Markdown."""
    Total_Cambios = 0
    Archivos_Modificados = []

    for Ruta_Archivo in sorted(CARPETA_FUENTES.glob("*.md")):
        Cambios = Procesar_Archivo(Ruta_Archivo)
        if Cambios:
            Total_Cambios += Cambios
            Archivos_Modificados.append((Ruta_Archivo, Cambios))

    print("=== LIMPIEZA DE CARACTERES Y NORMALIZACIÓN PDF ===")
    for Ruta_Archivo, Cambios in Archivos_Modificados:
        print(f"- {Ruta_Archivo}: {Cambios} cambios")

    print(f"Total archivos modificados: {len(Archivos_Modificados)}")
    print(f"Total cambios estimados: {Total_Cambios}")

    return 0

if __name__ == "__main__":
    raise SystemExit(Main())
