# Protocolo de uso de Antigravity

## Objetivo

Evitar tareas demasiado amplias, lentas o costosas en contexto. Toda tarea debe ser específica, limitada por rutas y verificable.

## Plantilla obligatoria de tarea

```text
Objetivo:

Archivos a leer:

Archivos a modificar:

Archivos prohibidos:

Contexto permitido:

Skill aplicable:

Gate relacionado:

Salida esperada:

Verificación:

Commit:
```

## Reglas

1. No pedir “revisa todo el proyecto”.
2. No pedir “mejora todo el plan”.
3. No abrir carpetas completas si no es necesario.
4. No modificar más de 3 archivos por tarea salvo instrucción expresa.
5. No hacer commit sin aprobación del usuario.
6. No generar documentos finales sin pasar por auditoría.
7. No reescribir archivos completos si solo se necesita un ajuste parcial.
8. Si una tarea tarda demasiado, detenerse y reportar estado.

## Ejemplo de tarea correcta

```text
Objetivo:
Completar el resumen ejecutivo para la exposición final en Zaragoza Activa.

Archivos a leer:
@AGENTS.md
@docs_control/contexto_minimo_operativo.md
@docs_control/gates_entrega_sistreg.md
@.agent/skills/skill-resumen-ejecutivo/SKILL.md
@.agent/skills/skill-tono-plan-empresa/SKILL.md
@plan_empresa/00_resumen_ejecutivo.md
@plan_empresa/02_idea_negocio.md
@plan_empresa/06_5_economico_financiero.md

Archivos a modificar:
@respuestas_plan_empresa/00_resumen_ejecutivo.md

Archivos prohibidos:
@anexos/
@docs_base/
@_build/

Skill aplicable:
@.agent/skills/skill-resumen-ejecutivo/SKILL.md

Gate relacionado:
Gate 1 — Resumen ejecutivo completo

Salida esperada:
Resumen ejecutivo con versión para exposición y versión para Plan de Empresa.

Verificación:
Confirmar que no introduce datos no presentes en los archivos leídos.

Commit:
No hacer commit sin aprobación.
```

## Capacidades de lectura técnica (Consulta permanente)

1. **Google Drive**: Puedo leer archivos de Google Docs y **Google Sheets** directamente. Para ello, el usuario debe proporcionar el **ID del documento**.
2. **Formatos de archivo**:
   - **PDF**: Formato preferido para fuentes externas y materiales formativos.
   - **Markdown/Texto**: Formato preferido para documentación interna y respuestas.
   - **DOCX**: Legible, pero se recomienda convertir a PDF para asegurar la integridad de tablas y formatos complejos.
