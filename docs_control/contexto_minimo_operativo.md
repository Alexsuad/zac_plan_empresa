# Contexto mínimo operativo

## Regla general

Leer solo lo necesario para la tarea actual. No abrir todo el repositorio por defecto.
Las preguntas guía se leen de `plan_empresa/` y las respuestas reales se redactan en `respuestas_plan_empresa/`.

## Mapa de lectura por tipo de tarea

### 1. Resumen ejecutivo

Leer:
- `AGENTS.md`
- `docs_control/gates_entrega_zac.md`
- `.agent/skills/skill-resumen-ejecutivo/SKILL.md`
- `.agent/skills/skill-tono-plan-empresa/SKILL.md`
- `plan_empresa/00_resumen_ejecutivo.md`, si existe como guía
- `plan_empresa/02_idea_negocio.md`
- `plan_empresa/06_5_economico_financiero.md`
- `respuestas_plan_empresa/00_resumen_ejecutivo.md`

Modificar:
- `respuestas_plan_empresa/00_resumen_ejecutivo.md`

No leer:
- `docs_base/`
- `anexos/`
- `_build/`

### 2. Plan económico-financiero

Leer:
- `AGENTS.md`
- `docs_control/gates_entrega_zac.md`
- `.agent/skills/skill-plan-financiero/SKILL.md`
- `.agent/skills/skill-validacion-fuentes/SKILL.md`
- `plan_empresa/06_5_economico_financiero.md` (guía)
- `respuestas_plan_empresa/06_5_economico_financiero.md` (respuestas)
- `anexos/A09_plan_economico_financiero.md`, si existe
- `anexos/finanzas/`, solo si existe y la tarea lo requiere

Modificar:
- `respuestas_plan_empresa/06_5_economico_financiero.md`

No leer:
- todos los demás anexos;
- todo `docs_base/`;
- todo `plan_empresa/` (salvo el archivo de la tarea).

### 3. Completar un apartado del plan

Leer:
- `AGENTS.md`
- `.agent/skills/skill-rellenar-apartado-plan/SKILL.md`
- `.agent/skills/skill-tono-plan-empresa/SKILL.md`
- el archivo específico de `plan_empresa/` (guía)
- el archivo específico de `respuestas_plan_empresa/` (respuestas)
- el anexo relacionado, solo si aplica

Modificar:
- el archivo específico de `respuestas_plan_empresa/`

No leer:
- otros apartados completos salvo que se indiquen explícitamente.

### 4. Crear o completar un anexo

Leer:
- `AGENTS.md`
- `.agent/skills/skill-gestion-anexos/SKILL.md`
- `.agent/skills/skill-validacion-fuentes/SKILL.md`
- el archivo del anexo específico
- máximo 1 o 2 archivos fuente relacionados de `respuestas_plan_empresa/`

No leer:
- todos los anexos;
- todo `plan_empresa/`;
- todo `docs_base/`.

### 5. Auditoría final

Leer:
- `AGENTS.md`
- `docs_control/gates_entrega_zac.md`
- `docs_control/registro_decisiones.md`
- `.agent/skills/skill-auditoria-final/SKILL.md`

Primero usar terminal para listar archivos:
`find . -maxdepth 3 -type f | sort`

Luego abrir solo archivos concretos con problemas.

No leer todo de golpe.

## Regla de gates

Si un gate está aprobado, no volver a revisar su contenido completo salvo que:

- haya cambios posteriores;
- el usuario lo pida;
- una contradicción lo exija.
