# Workflow: Consolidar Documento Final

**Objetivo:** Ensamblar un documento único, limpio y formateado que contenga todo el Plan de Empresa listo para ser exportado, revisado u hospedado de manera conjunta, garantizando que solo se consolide si la auditoría previa es aprobatoria.

## Condiciones de Entrada
- El workflow `auditar-plan-completo.md` debe haberse ejecutado y obtenido un resultado `PASS`.
- Los gates asociados al cierre de todas las fases del plan deben estar en estado de completados ("DONE").

## Fases de ejecución

1. **Validación de Bloqueo:**
   Si la auditoría previa reportó fallas o existen "Pendientes", la ejecución se detiene y avisa al usuario, denegando la consolidación.

2. **Ejecución de Compilación:**
   Ejecutar `python3 scripts/compilar_plan_empresa.py`. Esto leerá secuencialmente los archivos dentro de `respuestas_plan_empresa/`, excluyendo la estructura de índice interna si está indicada.

3. **Verificación Post-Compilación:**
   Comprobar que el archivo `_build/plan_empresa_sistreg_completo.md` existe y no tiene un tamaño o formato incongruente.

4. **Registro de Consolidación:**
   Generar un log en la salida indicando los archivos incluidos.
