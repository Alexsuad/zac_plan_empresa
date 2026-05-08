# AGENTS.md — Reglas de trabajo del repositorio

## 1. Propósito del repositorio

Este repositorio contiene la documentación específica para construir el Plan de Empresa de Sistreg. 
La denominación Proyecto Logístico se mantiene únicamente como referencia interna/descriptiva del ámbito de actuación.

No es el repositorio del sistema agéntico reutilizable para crear planes de empresa. Ese sistema vive en `plan_empresa_producto`.

## 2. Separación obligatoria entre repositorios

- `plan_empresa_producto`: sistema reusable, plantillas, lógica agéntica general y metodología para múltiples proyectos.
- `zac_plan_empresa`: caso real, documentación específica y entrega del Plan de Empresa de Sistreg.

No convertir este repositorio en el producto genérico. Las reglas, skills y documentos de control creados aquí solo sirven para completar este plan específico.

## 3. Capacidades de lectura técnica
- **Google Drive**: Puedo leer archivos de Google Docs y **Google Sheets** directamente. Para ello, el usuario debe proporcionar el **ID del documento**.
- **PDF/Docx**: Procesamiento de archivos locales (preferencia PDF para integridad de datos).
- **Entorno**: Ejecución en WSL/Ubuntu y acceso a herramientas agénticas (NotebookLM).

## 4. Fuente de verdad

Las preguntas guía viven en:
- `plan_empresa/`

Los entregables deben cumplir con la estructura definida en `respuestas_plan_empresa/` y el contexto institucional de **Zaragoza Activa / CONVIERTE (ZAC)**.

Los anexos viven en:
- `anexos/`

Los documentos metodológicos viven en:
- `docs_base/`

La planificación, gates y decisiones viven en:
- `docs_control/`

Las fuentes de verdad externas y soporte viven en:
- `docs_convierte/`

Las habilidades específicas viven en:
- `.agent/skills/`

Las salidas consolidadas viven en:
- `_build/`

**Regla:** Nunca escribir respuestas reales dentro de `plan_empresa/`. Cuando se responda una pregunta del plan, se lee la guía en `plan_empresa/` y se escribe la respuesta en `respuestas_plan_empresa/`.

## 5. Tono documental

El tono debe ser:
- claro;
- profesional;
- realista;
- verificable;
- sin humo tecnológico;
- sin promesas exageradas;
- con lenguaje logístico entendible;
- orientado a un Plan de Empresa defendible ante **Zaragoza Activa / CONVIERTE (ZAC)**, entidad de apoyo, banco o administración.

### 5.1. Lenguaje comercial de Sistreg

Cuando se redacten o revisen pitch, propuesta de valor, storytelling, landing, dossier comercial, casos de uso, marketing, ventas o entregables, usar la skill:

- `.agent/skills/skill-lenguaje-comercial-sistreg/SKILL.md`

Y respetar la regla:

- En diagnóstico, dolor y coste del problema: usar léxico logístico profundo.
- En solución, entregable, implementación y soporte: usar léxico logístico profundo + tecnología superficial concreta.
- Usar palabras como sistema, automatización, automático, dashboard, panel, aviso automático, validación automática, actualización automática e IA cuando aporta valor.
- Evitar en primera capa comercial herramientas internas o detalles de construcción: Make, n8n, Python, SQL, API, webhook, backend, frontend, servidor, base relacional, script, pipeline, prompt, embedding.
- No basta con decir “panel”, “alertas” o “formulario”; debe explicarse qué ve el cliente, qué usa, qué ocurre automáticamente, quién recibe el aviso y qué mejora en el flujo logístico.

## 6. Uso híbrido obligatorio

Usar enfoque híbrido:
- **Terminal, Git o scripts** para tareas deterministas:
  - copiar archivos;
  - verificar tamaños;
  - consolidar documentos;
  - generar salidas;
  - hacer commits;
  - validar estructura.
- **IA / Antigravity** para:
  - redacción;
  - análisis;
  - auditoría;
  - coherencia;
  - detección de contradicciones;
  - síntesis estratégica.

## 7. Tecnología para anexos

Usar:
- **Markdown** para texto, matrices y anexos estratégicos.
- **CSV** para datos tabulares o comparativos.
- **XLSX** para finanzas.
- **Mermaid** para diagramas simples, flujos, organigramas o Gantt.
- **Python** para gráficos o automatizaciones verificables.
- **DOCX/PDF** para entrega final.
- **HTML** no se usa por ahora.

## 8. Reglas de edición

Antes de modificar archivos:
1. Identificar qué archivo se va a tocar.
2. Explicar qué se cambiará.
3. No borrar contenido útil sin justificarlo.
4. No inventar datos.
5. Marcar pendientes cuando falte información.
6. Mantener trazabilidad de decisiones relevantes.
7. Cerrar cada tarea con:
   - archivos modificados;
   - resumen de cambios;
   - verificación realizada;
   - próximos pasos.

## 9. Prohibido

- Mezclar este repositorio con `plan_empresa_producto`.
- Crear funcionalidades genéricas innecesarias.
- Crear agentes múltiples sin necesidad real.
- Crear MCP.
- Instalar skills externas sin revisión.
- Borrar anexos o fuentes sin revisión.
- Presentar hipótesis como hechos comprobados.
- Convertir `AGENTS.md` en un megaprompt.

## 10. Auditor de Linealidad Documental

### Rol y Responsabilidad
El Auditor de Linealidad Documental es responsable de garantizar que el Plan de Empresa sea un documento fluido, coherente y de extensión controlada. Su función es técnica y objetiva, basada en mediciones deterministas.

### Reglas de Actuación
- **Control de Sedes:** Asegurar que cada concepto estratégico reside únicamente en su sede principal definida en `docs_control/sedes_informacion_plan_empresa.yml`.
- **Detección de Bloat:** Identificar y proponer la eliminación de contenido redundante, introducciones repetitivas y explicaciones circulares.
- **Gate de Extensión:** Bloquear la compilación oficial si el documento supera los límites críticos de páginas definidos en la política.

### Herramientas
- Script: `scripts/auditar_linealidad_plan_empresa.py`
- Regla: `.agent/rules/05-linealidad-documental.md`
- Skill: `.agent/skills/skill-auditoria-linealidad-documental/SKILL.md`

## Uso eficiente de contexto

1. No revisar todo el repositorio salvo auditoría final explícita.
2. Antes de trabajar, declarar:
   - archivos a leer;
   - archivos a modificar;
   - archivos prohibidos;
   - skill aplicable;
   - gate relacionado.
3. Usar referencias explícitas con `@archivo` o `@carpeta`.
4. Leer solo los archivos necesarios para la tarea actual.
5. No abrir `docs_base/` completo salvo que la tarea lo requiera.
6. No abrir `anexos/` completo salvo que se esté trabajando un anexo específico.
7. No abrir `_build/` salvo tareas de consolidación.
8. No volver a validar cosas ya cerradas por un gate aprobado, salvo que haya cambios posteriores.
9. Para operaciones de archivos usar terminal, Git o scripts.
10. Para redacción, análisis y auditoría usar IA.
11. Cerrar cada tarea con verificación concreta, no con revisión general.
