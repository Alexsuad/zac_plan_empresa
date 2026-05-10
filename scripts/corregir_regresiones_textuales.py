# File: scripts/corregir_regresiones_textuales.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Aplicar reemplazos controlados de terminología y cifras.
# Rol: Auditor determinista de regresiones textuales.
# ──────────────────────────────────────────────────────────────────────

import os
import argparse
import subprocess
from typing import List, Tuple, Dict

# Lista exacta de patrones (Buscar, Reemplazar)
PATRONES: List[Tuple[str, str]] = [
    # Variantes de Piloto / MVP (Prioridad alta)
    ("Piloto / MVP", "Validación técnica acotada"),
    ("piloto / MVP", "validación técnica acotada"),
    ("Piloto/MVP", "Validación técnica acotada"),
    ("piloto/MVP", "validación técnica acotada"),
    
    # Variantes de Prudencia Financiera
    ("viabilidad financiera blindada", "viabilidad financiera reforzada bajo las hipótesis actuales"),
    ("viabilidad blindada", "viabilidad reforzada bajo las hipótesis actuales"),

    # Variantes con Negrita para Indicadores Financieros
    (
        "**Previsión de Ventas:** De 22.000 € en el primer semestre de actividad (2026) hasta alcanzar los 47.000 € en el tercer ejercicio.",
        "**Previsión de ventas:** 31.180 € en 2026, 59.500 € en 2027 y 70.100 € en 2028, bajo las hipótesis comerciales actuales."
    ),
    (
        "**Financiación:** 5.000 € de aportación propia, eliminando cualquier necesidad de endeudamiento bancario inicial.",
        "**Aportación inicial propia:** 9.278 €, sin deuda bancaria inicial, lo que permite afrontar la fase de validación con mayor margen de seguridad."
    ),
    (
        "**Resultado Neto:** Se proyecta un beneficio acumulado de aproximadamente 8.150 € tras los tres primeros años, con una evolución positiva de la tesorería que permite afrontar futuras mejoras tecnológicas.",
        "**Resultado neto:** 7.724 € en 2026, 11.864 € en 2027 y 17.654 € en 2028, con una tesorería final estimada de 14.883 €, 32.258 € y 55.766 € respectivamente."
    ),

    # Patrones Originales
    (
        "Previsión de Ventas: De 22.000 € en el primer semestre de actividad (2026) hasta alcanzar los 47.000 € en el tercer ejercicio.",
        "Previsión de ventas: 31.180 € en 2026, 59.500 € en 2027 y 70.100 € en 2028, bajo las hipótesis comerciales actuales."
    ),
    (
        "Financiación: 5.000 € de aportación propia, eliminando cualquier necesidad de endeudamiento bancario inicial.",
        "Aportación inicial propia: 9.278 €, sin deuda bancaria inicial, lo que permite afrontar la fase de validación con mayor margen de seguridad."
    ),
    (
        "Resultado Neto: Se proyecta un beneficio acumulado de aproximadamente 8.150 € tras los tres primeros años, con una evolución positiva de la tesorería que permite afrontar futuras mejoras tecnológicas.",
        "Resultado neto: 7.724 € en 2026, 11.864 € en 2027 y 17.654 € en 2028, con una tesorería final estimada de 14.883 €, 32.258 € y 55.766 € respectivamente."
    ),
    (
        "el mantenimiento de un colchón de seguridad de 2.000 € (ver **Capítulo 7**)",
        "el seguimiento de cobros por hitos y la aportación inicial propia prevista en el plan financiero (ver **Capítulo 6.5**)"
    ),
    (
        "Servicio pagado de implementación de un sistema mínimo funcional (MVP) y limpieza de datos operativos críticos.",
        "Primer servicio pagado para definir alcance, reglas, evidencias, puntos de bloqueo y una solución mínima controlada sobre un flujo concreto."
    ),
    (
        "Diagnóstico Operativo: Sesión técnica de 1.5h para identificar cuellos de botella y fugas de información administrativa.",
        "Diagnóstico inicial gratuito: Sesión breve y acotada para identificar bloqueos operativos con impacto económico y valorar si existe una oportunidad real de mejora."
    ),
    (
        "Mantenimiento y Mejora: Soporte mensual para asegurar la adopción de la herramienta y el ajuste continuo ante nuevos retos operativos del cliente.",
        "Implementación completa: Despliegue del sistema de control operativo acordado, con reglas, evidencias, tableros y validaciones adaptadas al proceso del cliente.\n4. Mantenimiento y evolución: Soporte mensual, ajustes, seguimiento y mejora continua dentro de límites definidos."
    ),
    ("sistema mínimo funcional (MVP)", "solución mínima controlada"),
    ("sistemas mínimos funcionales (MVP)", "soluciones mínimas controladas"),
    ("MVPs", "soluciones mínimas controladas"),
    ("MVP", "solución mínima controlada"),
    ("ROI rápido", "retorno potencial medible"),
    ("ROI inmediato", "retorno potencial medible"),
    ("control total", "mayor control"),
    ("Control Total", "Mayor control"),
    ("Visibilidad total", "Mayor visibilidad"),
    ("visibilidad total", "mayor visibilidad"),
    ("salud financiera excepcional", "indicadores financieros positivos bajo las hipótesis actuales"),
    ("La viabilidad financiera está blindada", "La viabilidad financiera se ve reforzada"),
    ("> [!NOTE]", ""),
    ("> [!IMPORTANT]", "")
]

# Configuración de exclusiones
DIR_EXCLUIDOS = {".git", "_build", "__pycache__", ".venv", "venv", "node_modules", ".mypy_cache", ".pytest_cache"}
EXT_PERMITIDAS = {".md", ".txt"}

def ejecutar_comando(comando: List[str]) -> str:
    try:
        result = subprocess.run(comando, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        return f"Error ejecutando comando: {e}"

def corregir_regresiones(apply: bool = False, paths: List[str] = None):
    total_escaneados = 0
    total_afectados = 0
    total_reemplazos = 0
    reporte_afectados = []
    conteo_patrones = {i + 1: 0 for i in range(len(PATRONES))}

    files_to_process = []

    if paths:
        # Modo rutas específicas
        for p in paths:
            if os.path.exists(p):
                if os.path.isfile(p):
                    files_to_process.append(p)
                else:
                    # Si es un directorio, lo recorremos
                    for root, dirs, files in os.walk(p):
                        dirs[:] = [d for d in dirs if d not in DIR_EXCLUIDOS]
                        for file in files:
                            files_to_process.append(os.path.join(root, file))
            else:
                print(f"WARNING: La ruta '{p}' no existe.")
    else:
        # Modo escaneo total (comportamiento original)
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in DIR_EXCLUIDOS]
            for file in files:
                files_to_process.append(os.path.join(root, file))

    for filepath in files_to_process:
        # Validar extensión
        if not any(filepath.endswith(ext) for ext in EXT_PERMITIDAS):
            continue
            
        total_escaneados += 1
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                contenido_original = f.read()
        except Exception as e:
            print(f"Error leyendo {filepath}: {e}")
            continue

        nuevo_contenido = contenido_original
        reemplazos_en_archivo = 0
        
        for idx, (buscar, reemplazar) in enumerate(PATRONES, 1):
            ocurrencias = nuevo_contenido.count(buscar)
            if ocurrencias > 0:
                nuevo_contenido = nuevo_contenido.replace(buscar, reemplazar)
                total_reemplazos += ocurrencias
                reemplazos_en_archivo += ocurrencias
                conteo_patrones[idx] += ocurrencias

        if reemplazos_en_archivo > 0:
            total_afectados += 1
            reporte_afectados.append((filepath, reemplazos_en_archivo))
            
            if apply:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(nuevo_contenido)
                except Exception as e:
                    print(f"Error escribiendo en {filepath}: {e}")

    # Obtener rama actual
    rama_actual = ejecutar_comando(["git", "branch", "--show-current"]).strip()

    # Generar Reporte
    print("\n" + "="*50)
    print(" REPORTE DE CORRECCIÓN DE REGRESIONES")
    print("="*50)
    print(f"Rama actual: {rama_actual}")
    print(f"Modo: {'APLICAR CAMBIOS' if apply else 'DRY_RUN (SIMULACIÓN)'}")
    print(f"Archivos escaneados: {total_escaneados}")
    print(f"Archivos afectados: {total_afectados}")
    print(f"Total de reemplazos detectados: {total_reemplazos}")
    print("-" * 50)
    
    if reporte_afectados:
        print("Archivos afectados y número de cambios:")
        for path, count in reporte_afectados:
            print(f"  - {path}: {count} reemplazos")
    else:
        print("No se detectaron patrones para reemplazar en las rutas indicadas.")

    print("-" * 50)
    print("Conteo por patrón detectado:")
    for idx, count in conteo_patrones.items():
        if count > 0:
            print(f"  Patrón {idx}: {count} ocurrencias")

    print("-" * 50)
    # Reportar patrones financieros que NO encontraron coincidencia (Patrones 1, 2, 3)
    patrones_financieros_missing = []
    for i in [1, 2, 3]:
        if conteo_patrones[i] == 0:
            patrones_financieros_missing.append(i)
    
    if patrones_financieros_missing:
        print(f"Patrones financieros (1, 2, 3) sin coincidencia: {patrones_financieros_missing}")

    print("-" * 50)
    print("GIT STATUS:")
    print(ejecutar_comando(["git", "status", "--short"]))
    print("="*50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Corregir regresiones textuales.")
    parser.add_argument("--dry-run", action="store_true", help="Ejecutar sin aplicar cambios.")
    parser.add_argument("--apply", action="store_true", help="Aplicar cambios definitivos.")
    parser.add_argument("--paths", nargs="+", help="Rutas específicas para escanear.")
    
    args = parser.parse_args()
    
    if args.apply:
        corregir_regresiones(apply=True, paths=args.paths)
    else:
        corregir_regresiones(apply=False, paths=args.paths)
