# Plan de Poda Documental — Sistreg

**Estado:** PROPUESTA (Pendiente de Aprobación)
**Fecha:** 2026-05-08
**Referencia:** `_build/reportes/auditoria_linealidad_plan_empresa.md`

> [!IMPORTANT]
> Este documento es una **propuesta técnica**. No se deben ejecutar cambios sobre el contenido de `respuestas_plan_empresa/` hasta que cada acción sea validada por el usuario.

## 1. Diagnóstico de Bloat (Sobre-extensión)

El plan actual tiene una extensión estimada de **120.5 páginas**, excediendo el límite crítico de **70 páginas**. La causa principal es la fragmentación del conocimiento: cada capítulo se comporta como un documento independiente, repitiendo la identidad de la empresa, el concepto Doc-to-Cash y la trayectoria del promotor.

## 2. Matriz de Acciones y Recomendaciones

| Archivo Afectado | Problema Detectado | Acción Propuesta | Sede Correcta (Destino) | Prioridad | Riesgo Pérdida | Aprob. Requerida |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `00_resumen_ejecutivo.md` | Actúa como "mini plan" (8.4 pág). | **Resumir a Síntesis** | `02_idea_negocio.md` (Identidad) | Alta | Bajo | Sí |
| `01_equipo_promotor.md` | Trayectoria redundante (6 secciones). | **Consolidar / Podar** | `01_equipo_promotor.md` | Alta | Bajo | Sí |
| `02_idea_negocio.md` | Contiene intro dispersa. | **Centralizar Identidad** | `02_idea_negocio.md` | Alta | Bajo | Sí |
| `03_3_analisis_interno.md` | Extensión excesiva (9.5 pág). | **Poda del 50%** | `03_3_analisis_interno.md` | Alta | Medio | Sí |
| `04_dafo_came.md` | Justificaciones largas. | **Resumir a Tabla** | `04_dafo_came.md` | Alta | Bajo | Sí |
| `05_obj_lineas_est.md` | Conceptos financieros. | **Mover a Sede** | `06_5_econ_fin.md` | Alta | Bajo | Sí |
| `06_0_marca_naming.md` | Intro de Sistreg repetida. | **Eliminar / Referencia**| `02_idea_negocio.md` | Alta | Bajo | Sí |
| `06_1_marketing_ventas.md` | 12 pág de tácticas. | **Resumir** | `06_1_marketing_ventas.md` | Media | Bajo | Sí |
| `06_2_operaciones.md` | Explicación Doc-to-Cash dispersa. | **Centralizar Táctica** | `06_2_operaciones.md` | Alta | Bajo | Sí |
| `06_5_econ_fin.md` | Intros narrativas largas. | **Poda de Texto** | `06_5_econ_fin.md` | Alta | Crítico | Sí |

## 3. Matriz de Sedes Corregida (Centralización)

Se proponen los siguientes cambios de sede para normalizar la linealidad del documento:

### 3.1. Identidad e Introducción de Sistreg
- **Cambio de Sede Propuesto:** De `00_resumen_ejecutivo.md` a `02_idea_negocio.md`.
- **Motivo:** El resumen ejecutivo debe ser una síntesis; la "Idea de Negocio" es el lugar natural para la definición profunda de la identidad.
- **Riesgo:** Bajo. Mejora la jerarquía del plan.
- **Aprobación Requerida:** SÍ.

### 3.2. Concepto Doc-to-Cash (Táctica Operativa)
- **Cambio de Sede Propuesto:** De `05_objetivos_lineas_estrategicas.md` a `06_2_operaciones.md`.
- **Motivo:** Se identifica como un caso táctico operativo especializado, no solo como un objetivo estratégico de alto nivel.
- **Riesgo:** Bajo. Proporciona contexto técnico en el lugar donde se ejecuta la operación.
- **Aprobación Requerida:** SÍ.

### 3.3. Análisis Financiero y Resultados
- **Sede Principal:** `06_5_economico_financiero.md` (Contiene tablas, Excel y detalle).
- **En Resumen Ejecutivo:** Se reduce a una tabla de "Cifras Clave" y 1 párrafo de síntesis.
- **En Viabilidad (08):** Solo interpretación estratégica final del resultado.
- **Aprobación Requerida:** SÍ.

## 4. Riesgos Generales de la Poda

| Riesgo | Impacto | Mitigación |
| :--- | :--- | :--- |
| Incoherencia por referencias huérfanas | Medio | Revisar que al eliminar un párrafo no queden frases como "Como se mencionó anteriormente..." apuntando a nada. |
| Debilitamiento del equipo promotor | Bajo | Una síntesis potente de la trayectoria de Alexander es más eficaz que la repetición circular. |
| Omisión de hitos financieros | Medio | Asegurar que el Resumen Ejecutivo conserve los 3 KPIs maestros: Inversión, Punto de Equilibrio y Tesorería Año 3. |

## 5. Próximos Pasos (Workflow de Ejecución)

1. [ ] Aprobación de esta propuesta corregida.
2. [ ] Ejecución de la **Fase A**: Centralización de Identidad en `02_idea_negocio.md`.
3. [ ] Ejecución de la **Fase B**: Centralización de Doc-to-Cash en `06_2_operaciones.md`.
4. [ ] Ejecución de la **Fase C**: Poda de capítulos en Fail/Warning.
5. [ ] Re-auditoría final.

