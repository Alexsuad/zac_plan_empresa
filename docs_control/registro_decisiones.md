# Registro de Decisiones — Plan de Empresa Sistreg

### 2026-05-06 - Normalización final de reglas agénticas y soporte Red ARCE
- **Decisión**: Se establece **Sistreg** como marca única para el Plan de Empresa. La denominación Proyecto Logístico se mantiene únicamente como referencia interna/descriptiva del ámbito de actuación.
- **Acciones**:
  - servicio inicial como arranque guiado (eliminado "piloto").
  - diagnóstico inicial gratuito y no línea de ingreso.
  - prudencia financiera (no garantizar resultados).
  - Gates 2 y 3 actualizados a "En proceso avanzado".
  - skill-tono-plan-empresa con YAML válido y reglas reubicadas.
  - skill-plan-financiero alineada con Sistreg.
  - archivo informativo de Red ARCE como fuente operativa actual vía Google Sheets (incluido en .gitignore jerárquico).
- **Pendiente**:
  - Gráficos(Red ARCE) 09.04.2018.xls sigue pendiente crítico como archivo físico local.

| Fecha | Decisión | Motivo | Impacto | Archivos afectados | Responsable |
|---|---|---|---|---|---|
| 2026-05-04 | Separar `zac_plan_empresa` de `plan_empresa_producto`. | Evitar mezclar el sistema reusable con el caso real y específico de Sistreg. | Arquitectura del repositorio clara y aislada. | Raíz del repo, README, AGENTS.md | Antigravity |
| 2026-05-04 | Trabajar con archivos Markdown por apartado. | Facilitar la edición atómica, revisión por secciones y consolidación final. | Estructura en `plan_empresa/` y `respuestas_plan_empresa/`. | `plan_empresa/*.md`, `respuestas_plan_empresa/*.md` | Antigravity |
| 2026-05-04 | Usar anexos en Markdown/CSV/XLSX/Mermaid/Python. | Mantener edición simple, trazabilidad, soporte para datos financieros y conversión posterior. | Estructura de `anexos/`. | `anexos/`, `docs_base/` | Antigravity |
| 2026-05-04 | Priorizar resumen ejecutivo y plan económico-financiero. | Sistreg los requiere prioritariamente para la presentación y validación próxima. | Orden de ejecución en el Plan de Implementación. | `docs_control/plan_implementacion_entrega_sistreg.md` | Antigravity |
| 2026-05-04 | Usar enfoque híbrido. | Maximizar precisión técnica con terminal/scripts y calidad narrativa con IA. | Metodología de trabajo. | AGENTS.md, README.md | Antigravity |
| 2026-05-04 | Crear skills locales. | Evitar dependencia de skills externas, personalización total al proyecto Sistreg y mayor control. | `.agent/skills/` | `.agent/skills/` | Antigravity |
| 2026-05-04 | No convertir `zac_plan_empresa` en sistema genérico. | Mantener el foco absoluto en la entrega del Plan de Empresa de Sistreg. | Alcance del proyecto. | Todo el repositorio. | Antigravity |
| 2026-05-04 | Separar preguntas guía de respuestas reales. | Evitar que las preguntas del método ensucien la redacción final del proyecto. | `plan_empresa/` (preguntas) vs `respuestas_plan_empresa/` (respuestas). | `plan_empresa/`, `respuestas_plan_empresa/` | Antigravity |
| 2026-05-04 | Diferenciar tres índices operativos. | Claridad sobre qué documento se está consultando: guía, respuestas o estructura final. | Creación de índices específicos. | `docs_base/`, `plan_empresa/`, `respuestas_plan_empresa/` | Antigravity |
