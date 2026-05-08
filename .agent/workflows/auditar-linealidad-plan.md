# File: .agent/workflows/auditar-linealidad-plan.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Workflow para la auditoría de linealidad.
# Rol: Proceso estandarizado para el agente.
# ──────────────────────────────────────────────────────────────────────

# Workflow: Auditoría de Linealidad y Extensión

## Fase 1: Preparación
- Asegurarse de que todos los archivos en `respuestas_plan_empresa/` estén guardados.
- Verificar que los archivos de configuración en `docs_control/` existan.

## Fase 2: Ejecución Técnica
- Ejecutar: `python3 scripts/auditar_linealidad_plan_empresa.py`
- Capturar la salida estándar para ver el resumen rápido.

## Fase 3: Revisión de Hallazgos
- Leer `_build/reportes/auditoria_linealidad_plan_empresa.md`.
- Listar los 3 archivos con mayor exceso de extensión.
- Listar los 3 conceptos más "dispersos" (fuera de sede).

## Fase 4: Comunicación
- Informar al usuario del estado global (`LINEALIDAD_PASS`, `LINEALIDAD_WARNING`, `LINEALIDAD_FAIL`).
- Si hay `LINEALIDAD_FAIL`, el workflow se detiene y se debe ejecutar el "Workflow de Poda Documental".
