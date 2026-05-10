# File: scripts/auditar_formato_markdown_entrega.py

from pathlib import Path
import re
from typing import List, Tuple

CARPETA_FUENTES = Path("respuestas_plan_empresa")
RUTA_REPORTE = Path("_build/reportes/auditoria_formato_markdown_entrega.md")

# Patrones pensados para detectar listas pegadas en párrafos.
# No modifican archivos; solo alertan para revisión humana.
PATRONES = [
    ("lista_numerada_tras_dos_puntos", re.compile(r":\s+1\.\s+")),
    ("lista_numerada_multiple_en_linea", re.compile(r"\b1\.\s+.+\b2\.\s+")),
    ("lista_numerada_2_3_en_linea", re.compile(r"\b2\.\s+.+\b3\.\s+")),
    ("lista_con_guion_tras_dos_puntos", re.compile(r":\s+-\s+")),
    ("lista_con_guion_tras_punto", re.compile(r"\.\s+-\s+")),
    ("lista_con_asterisco_tras_dos_puntos", re.compile(r":\s+\*\s+")),
    ("lista_con_asterisco_tras_punto", re.compile(r"\.\s+\*\s+")),
]

def Recortar_Texto(Texto: str, Limite: int = 220) -> str:
    """Devuelve un fragmento corto para que el reporte sea fácil de leer."""
    Texto_Limpio = " ".join(Texto.strip().split())
    if len(Texto_Limpio) <= Limite:
        return Texto_Limpio
    return Texto_Limpio[:Limite] + "..."

def Auditar_Archivo(Ruta_Archivo: Path) -> List[Tuple[str, int, str, str]]:
    """Busca patrones de listas incrustadas dentro de un archivo Markdown."""
    Hallazgos = []
    try:
        Contenido = Ruta_Archivo.read_text(encoding="utf-8")
    except Exception:
        return []
        
    Lineas = Contenido.splitlines()

    for Numero_Linea, Linea in enumerate(Lineas, start=1):
        Linea_Limpia = Linea.strip()
        Linea_Anterior = Lineas[Numero_Linea - 2].strip() if Numero_Linea > 1 else ""

        # 1. Detectar si una lista comienza sin línea en blanco previa
        # (Excluyendo si es el inicio del archivo o sigue a un encabezado o a otro item de lista)
        Match_Lista = re.match(r"^(\d+\.|-|\*)\s+", Linea_Limpia)
        if Match_Lista:
            Es_Item_Lista_Anterior = re.match(r"^(\d+\.|-|\*)\s+", Linea_Anterior)
            if Linea_Anterior and not Linea_Anterior.startswith("#") and not Es_Item_Lista_Anterior:
                Hallazgos.append(
                    (
                        str(Ruta_Archivo),
                        Numero_Linea,
                        "lista_sin_linea_en_blanco_previa",
                        Recortar_Texto(Linea_Limpia),
                    )
                )
            continue

        # Saltar líneas vacías o encabezados para el resto de checks.
        if not Linea_Limpia or Linea_Limpia.startswith("#"):
            continue

        # 2. Detectar listas incrustadas en la misma línea
        for Nombre_Patron, Patron in PATRONES:
            if Patron.search(Linea_Limpia):
                Hallazgos.append(
                    (
                        str(Ruta_Archivo),
                        Numero_Linea,
                        Nombre_Patron,
                        Recortar_Texto(Linea_Limpia),
                    )
                )

    return Hallazgos

def Escribir_Reporte(Hallazgos: List[Tuple[str, int, str, str]]) -> None:
    """Escribe el reporte de auditoría en _build/reportes/."""
    RUTA_REPORTE.parent.mkdir(parents=True, exist_ok=True)

    Lineas_Reporte = [
        "# Auditoría de formato Markdown para entrega",
        "",
        "Objetivo: detectar listas numeradas o con viñetas incrustadas dentro de párrafos.",
        "",
    ]

    if not Hallazgos:
        Lineas_Reporte.extend([
            "## Resultado",
            "",
            "PASS - No se detectaron listas incrustadas sospechosas.",
            "",
        ])
    else:
        Lineas_Reporte.extend([
            "## Resultado",
            "",
            "FAIL - Se detectaron posibles listas incrustadas en párrafos.",
            "",
            "## Hallazgos",
            "",
        ])

        for Ruta, Numero_Linea, Nombre_Patron, Fragmento in Hallazgos:
            Lineas_Reporte.extend([
                f"### {Ruta}:{Numero_Linea}",
                "",
                f"- Patrón: `{Nombre_Patron}`",
                f"- Fragmento: `{Fragmento}`",
                "",
            ])

    RUTA_REPORTE.write_text("\n".join(Lineas_Reporte), encoding="utf-8")

def Main() -> int:
    """Ejecuta la auditoría sobre las fuentes Markdown del plan."""
    Hallazgos_Totales = []

    if not CARPETA_FUENTES.exists():
        print(f"Error: No se encuentra la carpeta {CARPETA_FUENTES}")
        return 1

    for Ruta_Archivo in sorted(CARPETA_FUENTES.glob("*.md")):
        Hallazgos_Totales.extend(Auditar_Archivo(Ruta_Archivo))

    Escribir_Reporte(Hallazgos_Totales)

    if Hallazgos_Totales:
        print("AUDITORIA_FORMATO_MARKDOWN_FAIL")
        print(f"Hallazgos: {len(Hallazgos_Totales)}")
        print(f"Reporte: {RUTA_REPORTE}")
        return 1

    print("AUDITORIA_FORMATO_MARKDOWN_PASS")
    print(f"Reporte: {RUTA_REPORTE}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(Main())
