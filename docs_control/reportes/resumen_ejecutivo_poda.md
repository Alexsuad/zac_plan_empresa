# Resumen Ejecutivo: Plan de Poda Documental — Sistreg

**Estado:** PENDIENTE DE APROBACIÓN EXPLÍCITA
**Objetivo:** Reducir la extensión de **120.5** a **< 70** páginas (Reducción estimada: ~42%).

## 1. Fases Propuestas y Archivos Afectados

| Fase | Objetivo | Archivos Afectados |
| :--- | :--- | :--- |
| **Fase A: Identidad** | Centralizar la identidad en su sede correcta. | `00_resumen_ejecutivo.md`, `02_idea_negocio.md`, `06_0_marca_naming.md`. |
| **Fase B: Operativa** | Mover Doc-to-Cash a la sede táctica. | `05_obj_lineas_est.md`, `06_2_operaciones.md`. |
| **Fase C: Poda Crítica** | Reducir capítulos con extensión Fail/Warning. | `01_equipo_promotor.md`, `03_3_analisis_interno.md`, `04_dafo_came.md`, `06_1_marketing_ventas.md`, `06_5_econ_fin.md`. |

## 2. Reducción Esperada y Métricas
- **Extensión Actual:** 120.5 páginas (estimadas).
- **Meta:** 70 páginas (Límite FAIL).
- **Estrategia:** Eliminación de redundancias (6 introducciones idénticas) y síntesis de tablas narrativas en `04_dafo_came.md` y `06_5_econ_fin.md`.

## 3. Riesgos Principales
1. **Referencias Huérfanas:** Riesgo de que párrafos eliminados dejen enlaces lógicos rotos ("Como se explica en la intro...").
2. **Síntesis Financiera:** Riesgo de omitir KPIs críticos en el Resumen Ejecutivo al podar tablas.
3. **Pérdida de Matices:** En `03_3_analisis_interno.md`, la poda agresiva (50%) requiere cuidado para no eliminar ventajas competitivas clave.

## 4. Decisiones que requieren Aprobación Explícita
- **Cambio de Sede de Identidad:** Dejar el Resumen Ejecutivo como síntesis y mover la carga técnica a `02_idea_negocio.md`.
- **Reubicación de Doc-to-Cash:** Tratarlo como una táctica operativa en `06_2_operaciones.md` en lugar de un objetivo general.
- **Poda del Equipo Promotor:** Consolidar las 6 menciones a la trayectoria de Alexander en un solo bloque potente.

## 5. Archivos que NO se tocarán
- **`03_1_analisis_externo.md`**: Se mantiene intacto (estado Warning leve, aceptable por ahora).
- **`07_implantacion_puesta_marcha.md`**: No se toca (está incompleto, no aporta al bloat actual).
- **`08_viabilidad_conclusiones.md`**: No se toca (está incompleto).
- **Cualquier archivo de soporte** en `docs_trabajo/` o `fuentes/`.

---
**Nota:** No se ejecutará ninguna acción sobre `respuestas_plan_empresa/` hasta que este resumen sea validado con la palabra: `Aprobado`.
