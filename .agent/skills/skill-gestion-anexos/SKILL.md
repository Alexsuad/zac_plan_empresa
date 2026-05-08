---
name: skill-gestion-anexos
description: Decide y estructura anexos del Plan de Empresa de Sistreg.
---

# Propósito

Gestionar qué información debe ir en el cuerpo principal del plan y qué información debe ir en anexos.

# Cuándo usarla

Usar al crear, completar o revisar anexos.

# Entradas esperadas

- Apartado del plan relacionado.
- Tipo de anexo requerido.
- Datos, matriz, tabla o evidencia disponible.

# Salida esperada

Anexo claro, trazable y conectado con el Plan de Empresa.

# Reglas

- El cuerpo principal contiene conclusiones.
- El anexo contiene evidencia, tablas largas, matrices, fuentes o soporte.
- Usar Markdown para anexos estratégicos.
- Usar CSV para datos tabulares grandes.
- Usar XLSX para finanzas.
- Usar Mermaid para diagramas simples.
- Usar Python solo para gráficos o automatizaciones verificables.
- No usar HTML por ahora.
- No crear anexos innecesarios.

# Límites

No duplicar información sin propósito.

# Verificación

Comprobar:
- anexo tiene título claro;
- está relacionado con un apartado;
- su formato es adecuado;
- no contradice el plan.


## Refuerzo de Control

- **Condición de salida:** Anexo documentado y vinculado en el inventario.
- **Estado final permitido:** Anexo Disponible o Pendiente.
- **Evidencia requerida:** Entrada en `docs_control/inventario_anexos_y_graficos.md` actualizada.
- **Caso de bloqueo:** Anexo mencionado en texto pero inexistente en el directorio `anexos/`.
- **Ejemplo mínimo de uso:** Registrar el Anexo A01 y asegurar que existe en `anexos/A01.md`.
