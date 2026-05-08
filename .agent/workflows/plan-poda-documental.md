# File: .agent/workflows/plan-poda-documental.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Workflow para generar un plan de poda basado en auditoría.
# Rol: Proceso de remediación estandarizado.
# ──────────────────────────────────────────────────────────────────────

# Workflow: Plan de Poda Documental

## Disparador
- Resultado `LINEALIDAD_FAIL` o `LINEALIDAD_WARNING` en la auditoría de linealidad.

## Fase 1: Diagnóstico Profundo
- Analizar los párrafos duplicados reportados.
- Analizar los excesos de palabras por archivo.
- Identificar introducciones repetitivas.

## Fase 2: Generación de Propuestas
Para cada hallazgo, definir una acción:
- **SINTETIZAR:** Reducir texto sin perder significado.
- **REFERENCIAR:** Sustituir explicación por "Ver Cap X.X".
- **ELIMINAR:** Borrar contenido redundante o irrelevante.
- **MOVER:** Trasladar contenido a su sede correcta.

## Fase 3: Creación de Artefacto de Salida
- Generar el archivo `docs_control/reportes/plan_poda_documental.md`.
- **IMPORTANTE:** Este archivo es solo una propuesta. NO aplicar los cambios hasta que el usuario apruebe el plan de poda.

## Fase 4: Presentación
- Mostrar al usuario un resumen de cuántas palabras se ahorrarían si se aplica el plan.
