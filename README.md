# Plan de Empresa — Sistreg
Este repositorio contiene la documentación específica para la elaboración del **Plan de Empresa de Sistreg**.

## IMPORTANTE
- **Sistreg** es la marca provisional de trabajo del proyecto.
- La denominación **Proyecto Logístico** se mantiene únicamente como referencia interna/descriptiva del ámbito de actuación.
- El sistema genérico de creación de planes de empresa vive en el repositorio: `plan_empresa_producto`.
- Este repositorio utiliza reglas, skills y documentos de apoyo específicos para completar, auditar y consolidar el plan de Sistreg.

## Reglas Críticas Sistreg
- **Marca**: Sistreg es marca provisional; Proyecto Logístico solo referencia interna/descriptiva. ZAC/Zaragoza Activa solo contexto institucional.
- **Servicio**: El primer servicio pagado se llama "arranque guiado"; no usar "piloto pagado" comercialmente.
- **Ingresos**: El diagnóstico inicial es gratuito, limitado y NO es línea de ingreso.
- **Modelo Económico**: Basado en las 5 líneas de control de `docs_control/regla_modelo_economico_servicios_sistreg.md`.
- **Prudencia**: No garantizar cifras, ROI ni ayudas. Sistreg no es marca registrada.

## Reenfoque comercial y lenguaje

El proyecto debe mantenerse alineado con el reenfoque comercial de Sistreg:

- Sistreg se presenta como automatización operativa especializada en logística.
- Evalúa procesos logísticos críticos, identifica el coste de sus bloqueos y diseña soluciones tecnológicas ligeras y a medida.
- El cliente debe entender qué recibe: sistema, panel, dashboard, automatizaciones, avisos automáticos, formularios o enlaces sencillos cuando aplique.
- No se deben ocultar la automatización ni la tecnología cuando forman parte del entregable.
- No se deben usar tecnicismos internos en la primera capa comercial: Make, n8n, Python, SQL, API, webhook, backend, frontend, etc.

Regla de lenguaje:
**Logística profunda para demostrar criterio. Automatización visible para explicar valor. Tecnicismos internos solo para documentación interna.**

Referencia:
- `docs_control/regla_lenguaje_comercial_sistreg.md`
- `.agent/skills/skill-lenguaje-comercial-sistreg/SKILL.md`

## Estructura del repositorio

- `plan_empresa/`: Preguntas guía del Plan de Empresa.
- `respuestas_plan_empresa/`: Respuestas reales redactadas del proyecto Sistreg.
- `anexos/`: Soporte, matrices, fuentes y evidencias (DAFO, PESTEL, etc.).
- `docs_base/`: Metodología, mapas, arquitectura documental y documentos de referencia.
- `docs_control/`: Control operativo, planificación, gates y registro de decisiones.
- `docs_convierte/`: Fuentes externas de soporte, materiales de formación, CVs resumidos e investigaciones.
- `.agent/skills/`: Skills locales para el asistente Antigravity.
- `_build/`: Salidas consolidadas y documentos generados para entrega.

**Regla:** Las respuestas reales nunca se escriben en `plan_empresa/`.

## Metodología de trabajo

Se sigue un enfoque **híbrido**:
- **Tareas deterministas** (copiar, consolidar, validar estructura) mediante terminal y scripts.
- **Tareas cognitivas** (redacción, análisis, auditoría estratégica) mediante IA (Antigravity).

Para más detalles sobre las reglas de trabajo, consultar [AGENTS.md](AGENTS.md).

## Recursos y Enlaces Externos
- [Plan Económico y Financiero (Google Sheets)](https://docs.google.com/spreadsheets/d/1P0i6Pi0s2tpkCj2z-z4eqrPogovvA5VkFVZyHe9dy6U/edit?usp=drive_link)

## Scripts de calidad documental

El proyecto cuenta con herramientas automáticas para garantizar la integridad y profesionalidad del documento final:

1. `scripts/compilar_plan_empresa.py`
   - Compila las fuentes Markdown de `respuestas_plan_empresa/`.
   - Genera el plan consolidado en `_build/test/` cuando se usa `--test`.
   - Produce los formatos MD, DOCX y PDF.

2. `scripts/verificar_plan_final_entrega.py`
   - Gate principal de cierre.
   - Verifica cifras financieras, términos sensibles, regresiones textuales y condiciones mínimas de entrega.
   - Debe ejecutarse antes de considerar el documento listo para revisión visual.

3. `scripts/limpiar_caracteres_pdf.py`
   - Normaliza caracteres invisibles, espacios problemáticos y residuos Unicode que pueden afectar el renderizado del PDF.
   - Debe ejecutarse antes de compilar o auditar el documento final.

4. `scripts/auditar_formato_markdown_entrega.py`
   - Detecta listas incrustadas en párrafos o listas sin separación previa.
   - Evita que el PDF/DOCX muestre listas pegadas dentro de bloques de texto.

5. `scripts/auditar_texto_corrupto_entrega.py`
   - Detecta texto corrupto, concatenaciones accidentales y patrones visuales prohibidos.
   - Ejemplos: `deEl`, `RutinLa`, `dCMRs`, `e-CMR`, caracteres Unicode de reemplazo y glifos raros de renderizado.

## Flujo recomendado antes de revisar el PDF

Antes de realizar una revisión visual humana del PDF, se debe ejecutar el siguiente pipeline de validación técnica:

```bash
python3 scripts/limpiar_caracteres_pdf.py
python3 scripts/auditar_formato_markdown_entrega.py
python3 scripts/compilar_plan_empresa.py --test
python3 scripts/verificar_plan_final_entrega.py
python3 scripts/auditar_texto_corrupto_entrega.py
```

> **Advertencia:** No editar directamente `_build/test/`. Las correcciones deben hacerse siempre en `respuestas_plan_empresa/`.

> **Advertencia:** No hacer commit, merge o push hasta que el PDF/DOCX haya pasado revisión visual humana.
