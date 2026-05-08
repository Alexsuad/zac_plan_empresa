# Workflow: Auditar Plan Completo

**Objetivo:** Verificar de forma exhaustiva y determinista el estado de desarrollo del Plan de Empresa, evaluando la completitud, coherencia textual y ausencia de apartados pendientes antes de proceder a cualquier consolidación o gate de entrega.

## Fases de ejecución

1. **Lectura de Estructura:** 
   El sistema identifica la estructura de archivos en `respuestas_plan_empresa/` a auditar.

2. **Ejecución Determinista de Auditoría:**
   Se utiliza el script `scripts/auditar_estado_plan_empresa.py` para generar una traza cuantificable sobre qué archivos contienen texto del tipo "Pendiente de completar".

3. **Ejecución de Coherencia Textual:**
   Se utiliza el script `scripts/auditar_coherencia_textual.py` para verificar que la terminología clave (Sistreg, torre de control, solución logística, validación técnica, etc.) esté correctamente empleada y no haya términos obsoletos.

4. **Revisión de Anexos y Gráficos:**
   Validar que los elementos mencionados en `docs_control/inventario_anexos_y_graficos.md` que tienen el estado de "Disponible" correspondan con archivos reales en la estructura.

5. **Generación de Reporte:**
   Con los resultados obtenidos, el sistema determina un estado global (PASS/FAIL) y detalla qué apartados exactos bloquean la entrega.
