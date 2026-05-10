# File: scripts/verificar_plan_final_entrega.py
# Verifica el documento final generado sin editarlo.
# El objetivo es detectar regresiones críticas antes de aprobar entrega.

from pathlib import Path
import re
import sys

DOCUMENTO_FINAL = Path("_build/test/plan_empresa_sistreg_completo.md")

PATRONES_FAIL = [
    r"22\.000",
    r"47\.000",
    r"8\.150",
    r"5\.000 €",
    r"\bMVP\b",
    r"\bMVPs\b",
    r"Piloto\s*/\s*MVP",
    r"Piloto/MVP",
    r"ROI inmediato",
    r"ROI rápido",
    r"control total",
    r"Control Total",
    r"Visibilidad total",
    r"visibilidad total",
    r"salud financiera excepcional",
    r"viabilidad blindada",
    r"una indicadores financieros",
    r"Garantiza un colchón",
    r"\[!NOTE\]",
    r"\[!IMPORTANT\]",
    r"Pendiente de completar",
]

PATRONES_WARNING = [
    r"autoempleo",
    r"\b[pP]iloto\w*",
    r"\bROI\b",
    r"\bPendiente\b",
]

def Buscar_Patrones(Texto: str, Patrones: list[str]) -> list[tuple[str, int, str]]:
    """Busca patrones y devuelve patrón, línea y contenido de línea."""
    Hallazgos = []

    Lineas = Texto.splitlines()
    for Numero_Linea, Linea in enumerate(Lineas, start=1):
        for Patron in Patrones:
            if re.search(Patron, Linea):
                Hallazgos.append((Patron, Numero_Linea, Linea.strip()))

    return Hallazgos

def Main() -> int:
    """Ejecuta la verificación del documento final generado."""
    if not DOCUMENTO_FINAL.exists():
        print(f"FAIL: no existe {DOCUMENTO_FINAL}")
        return 1

    Texto = DOCUMENTO_FINAL.read_text(encoding="utf-8")

    Hallazgos_Fail = Buscar_Patrones(Texto, PATRONES_FAIL)
    Hallazgos_Warning = Buscar_Patrones(Texto, PATRONES_WARNING)

    print("=== VERIFICACIÓN PLAN FINAL ===")
    print(f"Documento: {DOCUMENTO_FINAL}")
    print(f"Palabras aproximadas: {len(Texto.split())}")
    print()

    if Hallazgos_Fail:
        print("FAIL: se encontraron regresiones críticas:")
        for Patron, Linea, Contenido in Hallazgos_Fail:
            print(f"- Línea {Linea} | Patrón `{Patron}` | {Contenido}")
    else:
        print("PASS: no se encontraron regresiones críticas.")

    print()

    if Hallazgos_Warning:
        print("WARNING: revisar términos sensibles en contexto:")
        for Patron, Linea, Contenido in Hallazgos_Warning:
            print(f"- Línea {Linea} | Patrón `{Patron}` | {Contenido}")
    else:
        print("WARNING: sin términos sensibles pendientes.")

    return 1 if Hallazgos_Fail else 0

if __name__ == "__main__":
    raise SystemExit(Main())
