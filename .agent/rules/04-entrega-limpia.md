# 04. Entrega Limpia

- Los documentos finales, especialmente aquellos que se consolidarán en `_build/`, no pueden contener código no resuelto, variables sueltas, placeholders o texto marcado como "Pendiente de completar".
- Antes de marcar una fase o Gate como "DONE", se debe ejecutar una verificación determinista (mediante script u otra herramienta validada) para confirmar que el documento cumple con la estructura requerida y no tiene texto pendiente.
- Si la verificación falla, el Gate no puede considerarse "DONE".
