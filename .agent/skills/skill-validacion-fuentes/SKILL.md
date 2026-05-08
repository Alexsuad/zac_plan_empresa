---
name: skill-validacion-fuentes
description: Valida fuentes, datos y evidencias usadas en el Plan de Empresa.
---

# Propósito

Evitar que el Plan de Empresa use datos sin respaldo o afirmaciones no verificadas.

# Cuándo usarla

Usar al incorporar datos de mercado, competencia, sector, normativa, finanzas o ayudas.

# Entradas esperadas

- Fuente consultada.
- Dato extraído.
- Fecha de consulta.
- Apartado donde se usará.
- Nivel de confianza.

# Salida esperada

Fuente registrada y dato clasificado como hecho, hipótesis o pendiente.

# Reglas

- Priorizar fuentes oficiales, sectoriales o verificables.
- Registrar enlace, entidad, fecha y dato usado.
- Separar hecho, hipótesis y pendiente.
- No usar datos dudosos como si fueran hechos.
- Si una fuente no es suficiente, marcarla como apoyo contextual.

# Límites

No inventar enlaces, fechas ni cifras.

# Verificación

Comprobar:
- fuente identificada;
- dato usado explícito;
- fecha registrada;
- nivel de confianza asignado.


## Refuerzo de Control

- **Condición de salida:** Fuentes verificadas y citadas correctamente.
- **Estado final permitido:** Validado.
- **Evidencia requerida:** Enlaces funcionales o referencia a `docs_convierte/` u otras fuentes verificables.
- **Caso de bloqueo:** Datos inventados o referencias a documentos inexistentes.
- **Ejemplo mínimo de uso:** Verificar que el dato del TAM provenga de un informe real y no de la IA.
