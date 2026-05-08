# File: .agent/rules/05-linealidad-documental.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir las reglas de cumplimiento de linealidad documental.
# Rol: Regla del sistema para el agente.
# ──────────────────────────────────────────────────────────────────────

# Regla 05: Linealidad Documental y Control de Extensión

## Contexto
El Plan de Empresa de Sistreg es un documento único fragmentado. No es una colección de informes independientes. Para mantener la calidad y profesionalismo, se deben seguir estas reglas estrictas.

## Reglas Obligatorias

1. **Perspectiva de Capítulo Único**
   - Nunca escribas como si el lector no conociera el proyecto.
   - Evita frases como "Sistreg es una plataforma que...", "El proyecto Sistreg tiene como objetivo...".
   - Si necesitas introducir el contexto, asume que el lector ya leyó el Resumen Ejecutivo.

2. **Respeto a las Sedes de Información**
   - Antes de explicar un concepto, verifica si tiene una sede asignada en `docs_control/sedes_informacion_plan_empresa.yml`.
   - Si estás fuera de la sede principal, usa **referencias cruzadas** en lugar de explicaciones detalladas.
   - Ejemplo: "Como se detalla en el Plan de Operaciones (Cap. 6.3), la arquitectura de microservicios permite..." en lugar de volver a explicar la arquitectura.

3. **Control de Extensión (Word Count Management)**
   - Mantén los apartados dentro de los límites definidos en `docs_control/limites_extension_plan_empresa.yml`.
   - Prioriza la densidad de información sobre el volumen de palabras.
   - Si un capítulo excede las 2.000 palabras sin una justificación técnica (excepción), debe ser sintetizado.

4. **Eliminación de Redundancia Táctica**
   - No repitas los beneficios de "Doc-to-Cash" en cada sección de marketing, ventas y finanzas.
   - Explícalo a fondo en el Modelo de Negocio y menciónalo solo como motor de valor en el resto.

5. **Gate de Linealidad**
   - No se permite dar por finalizada una tarea de redacción sin ejecutar el script `scripts/auditar_linealidad_plan_empresa.py`.
   - Cualquier estado de `LINEALIDAD_FAIL` debe ser resuelto inmediatamente mediante poda o reestructuración.

## Cómo aplicar esta regla
Cada vez que el agente genere o modifique contenido en `respuestas_plan_empresa/`, debe auditar mentalmente si está violando la sede de información de otro capítulo.
