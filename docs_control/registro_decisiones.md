# Registro de Decisiones — Plan Empresa ZAC

| Fecha | Decisión | Motivo | Impacto | Archivos afectados | Responsable |
|---|---|---|---|---|---|
| 2026-05-04 | Separar `zac_plan_empresa` de `plan_empresa_producto`. | Evitar mezclar el sistema reusable con el caso real y específico de ZAC. | Arquitectura del repositorio clara y aislada. | Raíz del repo, README, AGENTS.md | Antigravity |
| 2026-05-04 | Trabajar con archivos Markdown por apartado. | Facilitar la edición atómica, revisión por secciones y consolidación final. | Estructura en `plan_empresa/`. | `plan_empresa/*.md` | Antigravity |
| 2026-05-04 | Usar anexos en Markdown/CSV/XLSX/Mermaid/Python. | Mantener edición simple, trazabilidad, soporte para datos financieros y conversión posterior. | Estructura de `anexos/`. | `anexos/`, `docs_base/` | Antigravity |
| 2026-05-04 | Priorizar resumen ejecutivo y plan económico-financiero. | ZAC los requiere prioritariamente para la presentación y validación próxima. | Orden de ejecución en el Plan de Implementación. | `docs_control/plan_implementacion_entrega_zac.md` | Antigravity |
| 2026-05-04 | Usar enfoque híbrido. | Maximizar precisión técnica con terminal/scripts y calidad narrativa con IA. | Metodología de trabajo. | AGENTS.md, README.md | Antigravity |
| 2026-05-04 | Crear skills locales. | Evitar dependencia de skills externas, personalización total al proyecto ZAC y mayor control. | `.agent/skills/` | `.agent/skills/` | Antigravity |
| 2026-05-04 | No convertir `zac_plan_empresa` en sistema genérico. | Mantener el foco absoluto en la entrega del Plan de Empresa logístico/ZAC. | Alcance del proyecto. | Todo el repositorio. | Antigravity |
