# Plan de Empresa — Sistreg

Este repositorio contiene la documentación específica para la elaboración del **Plan de Empresa de Sistreg**, orientado a su presentación en Zaragoza Activa (ZAC) y el programa Convierte.

## Descripción del proyecto

- **Proyecto:** Plan de Empresa Sistreg.
- **Objetivo:** Generar y mantener un plan de empresa profesional y defendible, basado en evidencias y validaciones reales.
- **Fuente principal:** Los capítulos vivos del plan se redactan de forma modular en `respuestas_plan_empresa/*.md`.
- **Salidas generadas:** El sistema compila estas fuentes para generar el documento consolidado en formatos Markdown, DOCX y PDF dentro de la carpeta `_build/test/`.

---

## Estructura del repositorio

- **`respuestas_plan_empresa/`**: Contiene los capítulos fuente del plan. Es el único lugar donde se debe redactar contenido del plan.
- **`docs_base/`**: Documentación de soporte, inventario de fuentes, referencias externas y materiales de investigación.
- **`docs_control/`**: Reglas de control, criterios de lenguaje comercial, decisiones de arquitectura y el modelo económico-financiero.
- **`scripts/`**: Herramientas de automatización para compilación, saneamiento, normalización y auditoría de calidad.
- **`_build/`**: Carpeta de salida para documentos generados. **No se versiona** y no debe editarse manualmente.
- **`anexos/`**: Documentación complementaria, matrices y evidencias que soportan las afirmaciones del plan.
- **`plan_empresa/`**: Contiene las preguntas guía originales (no se editan, solo sirven de referencia).

---

## Reglas Críticas Sistreg (Resumen)

- **Marca:** Sistreg es marca provisional; "Proyecto Logístico" es solo referencia descriptiva interna.
- **Servicio:** El primer servicio pagado es el "arranque guiado". El diagnóstico inicial es gratuito y limitado.
- **Modelo Económico:** Alineado con las 5 líneas de control de `docs_control/regla_modelo_economico_servicios_sistreg.md`.
- **Prudencia:** No garantizar cifras exactas, ROI ni ayudas externas.
- **Lenguaje Comercial:** Logística profunda para demostrar criterio + Automatización visible para explicar valor. Prohibido usar tecnicismos internos (Python, SQL, APIs) en capas comerciales.

---

## Scripts de calidad documental

El proyecto cuenta con herramientas permanentes para garantizar la integridad del documento final:

1. **`scripts/compilar_plan_empresa.py`**
   - Compila las fuentes de `respuestas_plan_empresa/`.
   - Genera `plan_empresa_sistreg_completo` en MD, DOCX y PDF en `_build/test/` (usar flag `--test`).

2. **`scripts/verificar_plan_final_entrega.py`**
   - Gate principal de cierre. Verifica cifras, términos sensibles y regresiones críticas.

3. **`scripts/limpiar_caracteres_pdf.py`**
   - Normaliza caracteres invisibles y residuos Unicode para asegurar un renderizado perfecto en PDF.

4. **`scripts/auditar_formato_markdown_entrega.py`**
   - Detecta errores de formato (listas pegadas, párrafos mal cerrados) que rompen la estética en PDF/DOCX.

5. **`scripts/auditar_texto_corrupto_entrega.py`**
   - Detecta patrones prohibidos o concatenaciones accidentales (ej: `deEl`, `RutinLa`, `dCMRs`, `e-CMR`).

6. **`scripts/normalizar_tipografia_pdf.py`**
   - Herramienta de apoyo para asegurar la consistencia tipográfica en el documento final.

7. **Herramientas de Remediación**
   - `scripts/corregir_regresiones_textuales.py` y `scripts/remediar_fuentes_plan_final.py`: Utilidades para correcciones masivas documentadas (no forman parte del flujo diario, solo uso puntual).

---

## Flujo recomendado antes de revisar PDF/DOCX

Para garantizar que el documento está listo para una revisión visual humana, se debe ejecutar obligatoriamente este pipeline:

```bash
python3 scripts/limpiar_caracteres_pdf.py
python3 scripts/auditar_formato_markdown_entrega.py
python3 scripts/compilar_plan_empresa.py --test
python3 scripts/verificar_plan_final_entrega.py
python3 scripts/auditar_texto_corrupto_entrega.py
```

> [!IMPORTANT]
> **No editar nunca** directamente los archivos en `_build/test/`. Si detectas un error, corrígelo en la fuente correspondiente dentro de `respuestas_plan_empresa/` y vuelve a ejecutar el flujo.

> **Advertencia:** No hacer commit, merge o push hasta que el PDF/DOCX haya pasado revisión visual humana.
