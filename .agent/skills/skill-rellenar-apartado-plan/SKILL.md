---
name: skill-rellenar-apartado-plan
description: Guía para completar apartados del Plan de Empresa sin borrar estructura ni perder información.
---

# Propósito

Redactar el contenido final del Plan de Empresa dentro de `respuestas_plan_empresa/`, listo para integrarse en el documento de entrega, manteniendo el tono profesional y la voz narrativa adecuada.

# Cuándo usarla

Usar cuando se trabaje un apartado concreto del Plan de Empresa.

# Entradas esperadas

- Archivo del apartado.
- Preguntas originales o estructura del apartado.
- Información disponible.
- Pendientes conocidos.

# Salida esperada

Apartado completado con:
- Texto final redactado para el Plan de Empresa.

## Clasificación previa de preguntas

Antes de redactar un apartado, las preguntas guía deben clasificarse para evitar inventar información, duplicar trabajo o pedir al usuario datos que ya existen en las fuentes internas.

Usar esta matriz de clasificación:

| Código | Significado | Uso |
|---|---|---|
| `[F]` | Fuente interna del proyecto | La respuesta ya existe en documentos internos: `docs_base/`, `respuestas_plan_empresa/`, `anexos/`, `docs_control/`, investigaciones previas o documentos financieros. No preguntar al usuario antes de revisar estas fuentes. |
| `[U]` | Usuario | La respuesta depende de una decisión personal, estratégica u operativa del promotor. Debe preguntarse al usuario. |
| `[I-SIMPLE]` | Consulta simple en internet | Dato puntual verificable con una fuente pública u oficial: ayudas, trámites, referencias normativas básicas, entidades o servicios institucionales. |
| `[I-DEEP]` | Investigación profunda | Tema que requiere varias fuentes, comparación y análisis: mercado, competencia, tendencias, normativa compleja, precios de referencia, barreras sectoriales o benchmarking. |
| `[M]` | Mixto | Requiere combinar fuentes internas, decisión del usuario, investigación externa o datos financieros. No debe responderse con una sola fuente. |
| `[NO-RESPONDER-AÚN]` | Validación futura | No debe inventarse ni cerrarse todavía. Depende de clientes reales, entrevistas, ventas, métricas, disposición de pago, ciclo comercial o resultados futuros. |

Reglas asociadas:
- Primero revisar fuentes internas.
- Después clasificar cada pregunta.
- Solo preguntar al usuario lo que sea `[U]` o la parte de usuario de `[M]`.
- Solo buscar en internet lo que sea `[I-SIMPLE]` o `[I-DEEP]`.
- No redactar como hecho lo que sea hipótesis.
- No responder todavía lo marcado como `[NO-RESPONDER-AÚN]`.
- Antes de redactar un apartado complejo, construir una matriz con: pregunta guía, estado, clasificación, fuente probable y acción necesaria.

# Reglas

- Las respuestas reales se redactan siempre en `respuestas_plan_empresa/`.
- `plan_empresa/` se consulta solo como guía cuando haga falta.
- No modificar `plan_empresa/` salvo tarea explícita de mantenimiento de preguntas.
- No mezclar preguntas y respuestas en el mismo archivo.
- No borrar preguntas útiles de la guía sin justificarlo.
- No inventar información.
- Marcar claramente lo pendiente en la respuesta.
- Relacionar el apartado con anexos cuando corresponda.
- Los apartados de `respuestas_plan_empresa/` deben redactarse en formato final (listo para entrega).
- **Sistreg** es la marca provisional; Proyecto Logístico solo referencia interna.
- El primer servicio pagado es "arranque guiado"; no usar "piloto pagado".
- No incluir secciones internas como "Datos usados" o "Pendientes" en respuestas finales.

# Límites

No modificar archivos en `plan_empresa/` durante la redacción de respuestas.

# Verificación

Comprobar:
- archivo modificado correcto;
- estructura conservada;
- pendientes marcados;
- sin contradicciones evidentes.


## Refuerzo de Control

- **Condición de salida:** Archivo `.md` en `respuestas_plan_empresa/` redactado según la guía.
- **Estado final permitido:** Borrador avanzado o Completado.
- **Evidencia requerida:** Archivo guardado sin destruir la estructura original solicitada.
- **Caso de bloqueo:** Inventar datos para rellenar campos obligatorios.
- **Ejemplo mínimo de uso:** Rellenar el equipo promotor usando el CV sin alucinar experiencia extra.
