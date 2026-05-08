---
name: skill-analisis-huecos
description: Compara guías con respuestas para detectar vacíos, clasificar el tipo de información faltante y ejecutar el protocolo de investigación.
---

# Propósito

Sistematizar el análisis de preguntas sin responder en cualquier apartado del Plan de Empresa, clasificándolas según la fuente de la información (usuario o internet) y ejecutando investigaciones solo con autorización previa.

# Cuándo usarla

- Cuando se requiera revisar qué falta por completar en un documento.
- Cuando el usuario indique que ha volcado todo lo que sabe y necesita avanzar.
- Antes de dar por cerrado un archivo de `respuestas_plan_empresa/`.

# Entradas esperadas

- Archivo de preguntas guía (`plan_empresa/XX_...md`).
- Archivo de respuestas actual (`respuestas_plan_empresa/XX_...md`).

# Salida esperada

1. Reporte de huecos clasificados.
2. Petición de datos al usuario (para lo que solo él sabe).
3. Solicitud de autorización de búsqueda (para lo investigable).
4. (Post-autorización) Hallazgos para validación y posterior integración.

# Flujo de ejecución (Pasos Obligatorios)

## Paso 1: Comparación
Comparar el contenido del archivo guía con el archivo de respuestas. Identificar todas las preguntas, secciones o conceptos que no han sido respondidos o están incompletos.

## Paso 2: Clasificación de los Huecos
Clasificar cada hueco detectado en una de estas tres categorías basándose en su importancia y complejidad:
- **[F] Fuente interna:** Información que ya existe en el repositorio (docs_base, otras respuestas, etc.).
- **[U] Usuario:** Información que solo el emprendedor puede decidir o conocer (ej. nombre de marca, inicio de operaciones, decisiones operativas internas).
- **[I-SIMPLE] Investigación Superficial:** Datos concretos, rápidos o definiciones que se encuentran fácilmente en internet (ej. direcciones de organismos, leyes generales).
- **[I-DEEP] Investigación Profunda:** Análisis complejo que requiere buscar en múltiples fuentes, cruzar datos o evaluar el mercado (ej. listado de competidores locales, tipos de clientes indirectos, tendencias del sector logístico).
- **[M] Metodología:** Preguntas que se resuelven aplicando una skill o regla del proyecto (ej. tono, lenguaje comercial).
- **[NO-RESPONDER-AÚN]:** Información que depende de una fase futura (ej. financiero detallado si no se ha validado el modelo).

## Paso 3: Presentación y Petición de Autorización (Gate)
Detenerse y presentar al usuario un reporte estructurado con las siguientes acciones:
1. Listar las preguntas **[U]** y pedir al usuario que las responda.
2. Listar las preguntas **[I-SIMPLE]** e **[I-DEEP]**, justificando por qué requieren investigación.
3. **Preguntar explícitamente:** "¿Me autorizas a buscar la información de las categorías [I-SIMPLE] e [I-DEEP] en internet para presentarte una propuesta?"

## Paso 4: Búsqueda y Validación
- **NO INICIAR NINGUNA BÚSQUEDA** hasta recibir la aprobación expresa del usuario.
- Una vez autorizado, usar las herramientas de búsqueda pertinentes según la clasificación.
- Presentar los resultados obtenidos al usuario para que los revise y decida qué es útil y qué se descarta.

## Paso 5: Integración Final
- Solo tras la aprobación del usuario de los hallazgos, inyectar el contenido en el archivo correspondiente de `respuestas_plan_empresa/`.
- Aplicar estrictamente las directrices de la `skill-tono-plan-empresa` (primera persona profesional o voz institucional, sin secciones internas ni formato de borrador).

# Reglas estrictas
- No asumir respuestas que dependan del usuario.
- No gastar tiempo de cómputo en búsquedas web sin autorización previa.
- Presentar la información encontrada como borrador para revisión, nunca escribirla directamente en el documento final a sus espaldas.


## Refuerzo de Control

- **Condición de salida:** Reporte de vacíos generado con clasificación de información faltante.
- **Estado final permitido:** PASS (sin vacíos) o FAIL (con listado de vacíos).
- **Evidencia requerida:** Log de ejecución con los apartados contrastados.
- **Caso de bloqueo:** Falta de acceso a las guías o a las respuestas.
- **Ejemplo mínimo de uso:** El agente lee `plan_empresa/02_idea.md` y `respuestas_plan_empresa/02_idea_negocio.md` y lista lo que falta.
