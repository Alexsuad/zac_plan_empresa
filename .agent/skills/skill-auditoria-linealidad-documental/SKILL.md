---
id: skill-auditoria-linealidad-documental
name: auditoria-linealidad-documental
description: Ejecuta y analiza la auditoría determinista de extensión, repetición y sedes de información del Plan de Empresa Sistreg.
version: 1.1
status: stable
last_update: 2026-05-09
author: Antigravity
dependencies:
  - scripts/auditar_linealidad_plan_empresa.py
  - docs_control/limites_extension_plan_empresa.yml
---

# File: .agent/skills/skill-auditoria-linealidad-documental/SKILL.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Habilidad para ejecutar y analizar la linealidad documental.
# Rol: Skill técnica del agente.
# ──────────────────────────────────────────────────────────────────────

# Skill: Auditoría de Linealidad Documental

## Propósito
Permite al agente medir con precisión la extensión del plan de empresa, detectar redundancias entre archivos y asegurar que cada concepto reside en su sede de información correcta.

## Cuándo usar esta skill
- Al finalizar la redacción de un capítulo.
- Antes de consolidar o compilar el plan completo.
- Cuando el usuario reporte que el documento se siente repetitivo o demasiado largo.

## Procedimiento de ejecución

### 1. Ejecución del Auditor
Ejecutar el script determinista para obtener el reporte base:
```bash
python3 scripts/auditar_linealidad_plan_empresa.py
```

### 2. Análisis del Reporte
Leer el archivo generado en `_build/reportes/auditoria_linealidad_plan_empresa.md` y evaluar:
- **Estado Global:** Si es `LINEALIDAD_FAIL`, identificar el motivo principal (páginas, intros o archivos específicos).
- **Sedes:** Identificar conceptos que se están explicando fuera de su sede principal.
- **Duplicados:** Revisar los párrafos con alto ratio de similitud (>0.78).

### 3. Propuesta de Acción (si hay fallos o avisos)
- **Para extensiones:** Proponer puntos de poda o síntesis.
- **Para sedes:** Reemplazar explicaciones redundantes por referencias breves al capítulo sede.
- **Para duplicados:** Unificar contenido o eliminar la repetición menos relevante.

## Salidas esperadas
- Reporte detallado de métricas.
- Plan de acción para recuperar la linealidad si se detectan desviaciones.
- Exit code 0 (Success/Warning) o 1 (Fail).
