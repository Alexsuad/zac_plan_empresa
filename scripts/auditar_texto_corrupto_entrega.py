# File: scripts/auditar_texto_corrupto_entrega.py
# Auditoría específica para detectar patrones de texto corrupto en las fuentes.

from pathlib import Path
import re
import sys

CARPETA_FUENTES = Path("respuestas_plan_empresa")
CONSOLIDADO = Path("_build/test/plan_empresa_sistreg_completo.md")

# Patrones detectados en la revisión visual
PATRONES_CORRUPTOS = [
    r"deEl",
    r"eEl",
    r"RutinLa",
    r"ConversiónEl",
    r"supeditadasEl",
    r"todLa",
    r"\*\*Sistreg opera",
    r"Económico-Financiero",
    r"económico-financiero",
    r"documental-económico",
    r"operativo-económica",
    r"operativo-económico",
    r"e-CMR",
    r"e-CMRs",
    r"eCMR",
    r"dCMRs",
    r"deCMRs",
    r"dCMR electrónico",
    r"dCMR electrónico electrónico",
    r"\uFFFD",
]

def Auditar_Texto(Ruta: Path, Texto: str) -> list[tuple[int, str, str]]:
    Hallazgos = []
    Lineas = Texto.splitlines()
    for Numero_Linea, Linea in enumerate(Lineas, start=1):
        for Patron in PATRONES_CORRUPTOS:
            if re.search(Patron, Linea):
                Hallazgos.append((Numero_Linea, Patron, Linea.strip()))
    return Hallazgos

def Main() -> int:
    Exito = True
    print("=== AUDITORÍA DE TEXTO CORRUPTO ===")
    
    # Revisar fuentes
    for Ruta in sorted(CARPETA_FUENTES.glob("*.md")):
        Hallazgos = Auditar_Texto(Ruta, Ruta.read_text(encoding="utf-8"))
        if Hallazgos:
            Exito = False
            print(f"FAIL: {Ruta}")
            for Linea, Patron, Contenido in Hallazgos:
                print(f"  - L{Linea} | Patrón `{Patron}` | {Contenido}")

    # Revisar consolidado si existe
    if CONSOLIDADO.exists():
        Hallazgos = Auditar_Texto(CONSOLIDADO, CONSOLIDADO.read_text(encoding="utf-8"))
        if Hallazgos:
            Exito = False
            print(f"FAIL: {CONSOLIDADO}")
            for Linea, Patron, Contenido in Hallazgos:
                print(f"  - L{Linea} | Patrón `{Patron}` | {Contenido}")
    else:
        print(f"INFO: No se encuentra consolidado para auditar: {CONSOLIDADO}")

    if Exito:
        print("PASS: No se detectaron patrones de texto corrupto.")
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(Main())
