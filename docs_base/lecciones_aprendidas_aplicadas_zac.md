# Lecciones Aprendidas Aplicadas a ZAC

Este documento resume las mejores prácticas extraídas de experiencias previas y adaptadas específicamente para la ejecución del Plan de Empresa ZAC.

## Principios de Diseño Agéntico y Documental

1. **Separación de Componentes**:
   - Mantener una distinción clara entre Agente (Antigravity), Skills (habilidades específicas), Reglas (instrucciones obligatorias) y Gates (puntos de control).
   - No intentar resolver problemas complejos únicamente creando nuevos agentes; priorizar skills acotadas.

2. **Skills Atómicas**:
   - Las skills deben ser pequeñas, con un propósito único, entradas/salidas definidas y criterios de verificación claros.

3. **Flujo Estratégico**:
   - Separar las fases de: **Investigación** → **Digestión Estratégica** → **Redacción** → **Auditoría**. No mezclar redacción con investigación en el mismo paso.

4. **Desarrollo Híbrido**:
   - Usar la terminal y scripts para tareas que requieran exactitud (conteo de palabras, validación de enlaces, consolidación).
   - Usar la IA para tareas que requieran juicio, tono y síntesis estratégica.

5. **Evidencia y Trazabilidad**:
   - No avanzar de fase o gate sin presentar evidencia clara (listado de archivos, resultados de scripts, validación de coherencia).
   - Registrar decisiones relevantes en el `registro_decisiones.md` para evitar "teléfonos rotos" o cambios de rumbo injustificados.

6. **Gestión del Contexto**:
   - No saturar el contexto del asistente. Trabajar con la información mínima necesaria para la tarea actual.
   - Evitar convertir archivos como `AGENTS.md` en megaprompts inmanejables.

7. **Higiene Documental**:
   - Cerrar cada tarea con un resumen de cambios y verificación.
   - Marcar explícitamente los pendientes y las hipótesis para evitar que se presenten como hechos comprobados.
