# AGENTS.md — Reglas de trabajo del repositorio

## Propósito del repositorio

Este repositorio contiene la documentación específica para construir el Plan de Empresa del proyecto logístico/ZAC.

No es el repositorio del sistema agéntico reutilizable para crear planes de empresa. Ese sistema vive en otro repositorio.

## Fuente de verdad

La documentación principal vive en:

- `plan_empresa/`

Los anexos, fuentes y material de soporte viven en:

- `anexos/`

Las salidas consolidadas generadas viven en:

- `_build/`

## Regla principal

No mezclar este caso real con el producto genérico de creación de planes de empresa.

Este repositorio debe mantenerse enfocado en el proyecto logístico/ZAC.

## Forma de trabajo

Usar enfoque híbrido:

- Terminal, Git o scripts para tareas deterministas: copiar archivos, verificar tamaños, consolidar documentos, generar salidas, hacer commits.
- IA / Antigravity para redacción, análisis, auditoría, estructura, coherencia y detección de contradicciones.

## Tono documental

El tono debe ser:

- claro,
- profesional,
- realista,
- verificable,
- sin humo tecnológico,
- sin promesas exageradas,
- con lenguaje logístico entendible.

## Estructura esperada de cada apartado

Cada archivo dentro de `plan_empresa/` debe mantener, cuando aplique, esta estructura:

1. Versión desarrollada
2. Versión para Plan de Empresa
3. Pendientes por validar
4. Anexos relacionados
5. Conclusión estratégica

## Reglas de edición

Antes de modificar archivos:

1. Identificar qué archivo se va a tocar.
2. Explicar qué se cambiará.
3. No borrar contenido útil sin justificarlo.
4. Mantener una copia o usar Git antes de cambios grandes.
5. Cerrar cada tarea con:
   - archivos modificados,
   - resumen de cambios,
   - verificación realizada,
   - próximos pasos.

## Prohibido

- Convertir este repositorio en el sistema agéntico general.
- Crear agentes, skills o workflows complejos sin necesidad real.
- Duplicar contenido sin propósito.
- Borrar anexos o información base sin revisión.
- Presentar hipótesis como hechos comprobados.
