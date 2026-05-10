# AGENTS.md — Protocolo Obligatorio para Agentes

Este documento establece las reglas de comportamiento, control y seguridad para cualquier agente de IA que opere en este repositorio. Su cumplimiento es **obligatorio y bloqueante**.

---

## 1. Propósito y Separación de Repositorios

- **`zac_plan_empresa`**: Caso real y específico del Plan de Empresa Sistreg.
- **`plan_empresa_producto`**: Sistema reutilizable y genérico de creación de planes.
- **Regla**: No convertir este repositorio en un producto genérico ni crear arquitectura post-MVP sin aprobación humana.

---

## 2. Reglas Obligatorias de Trabajo (Guardrails)

### 2.1. Qué NO se puede tocar (Prohibiciones)
- **Contenido del Plan**: No modificar el texto en `respuestas_plan_empresa/` salvo instrucción técnica.
- **Finanzas**: No modificar cifras financieras ni el Excel de soporte.
- **Carpeta `_build/`**: Prohibido editar o crear archivos manualmente aquí. Solo los scripts escriben en esta carpeta.
- **Archivos Ocultos**: No tocar `.git`, `.env` ni configuraciones del IDE.

### 2.2. Tono Documental y Lenguaje Sistreg
- **Tono**: Profesional, realista, verificable y sin promesas exageradas (Hype). Defendible ante ZAC/Convierte.
- **Lenguaje**: Logística profunda (criterio) + Automatización visible (valor).
- **Restricción Comercial**: No usar tecnicismos internos (Python, SQL, APIs, Make, n8n) en la primera capa comercial. Explicar siempre qué ve y qué gana el cliente.

---

## 3. Fuente de Verdad y Estructura

- **`plan_empresa/`**: Contiene preguntas guía. **REGLA: NUNCA escribir respuestas reales aquí.**
- **`respuestas_plan_empresa/`**: Fuente viva de respuestas reales.
- **`docs_base/`**: Documentación base y referencias.
- **`docs_control/`**: Reglas (Gates), decisiones y modelo económico.
- **`scripts/`**: Herramientas deterministas de calidad.
- **`_build/`**: Salidas generadas. **No se edita ni se versiona.**

---

## 4. Uso Híbrido y Eficiencia de Contexto

- **Enfoque Híbrido**: IA para redacción, análisis y auditoría cognitiva. Scripts/Terminal para tareas deterministas (copiar, validar, consolidar). No resolver con IA lo que puede verificar un script.
- **Gestión de Contexto**: No leer todo el repositorio. Leer solo archivos necesarios. Evidencia concreta al cerrar cada tarea.

---

## 5. Auditoría y Modelo Económico

- **Linealidad**: Usar `scripts/auditar_linealidad_plan_empresa.py` y la skill de auditoría para controlar el "bloat", la duplicidad y asegurar que la información reside en su sede correcta.
- **Modelo Económico**: Toda tarea sobre finanzas, costes o propuesta de valor debe alinearse con `docs_control/regla_modelo_economico_servicios_sistreg.md`.

---

## 6. Protocolo de Calidad Documental (Mínima Intervención)

1. **Detección**: Usar scripts para encontrar fallos.
2. **Propuesta**: Explicar el cambio técnico.
3. **Ejecución**: Aplicar solo en los archivos fuente afectados.
4. **Validación**: Re-ejecutar auditorías para confirmar la solución.

---

## 7. Comandos Obligatorios y Estados de Control

Antes de cerrar cualquier tarea técnica, el agente **DEBE** ejecutar y reportar:

```bash
python3 scripts/limpiar_caracteres_pdf.py
python3 scripts/auditar_formato_markdown_entrega.py
python3 scripts/compilar_plan_empresa.py --test
python3 scripts/verificar_plan_final_entrega.py
python3 scripts/auditar_texto_corrupto_entrega.py
```

### Estados válidos de flujo:
- `READY_FOR_VISUAL_REVIEW`
- `VISUAL_REVIEW_FAILED`
- `VISUAL_REVIEW_FAILED_MINOR_FIXES`
- `VISUAL_REVIEW_PASS`
- `READY_FOR_COMMIT_EN_RAMA`
- `COMMIT_SUCCESSFUL_EN_RAMA`
- `MAIN_LOCAL_READY_FOR_FINAL_PACKAGING`
- `READY_FOR_FINAL_PACKAGING`
- `READY_TO_PUSH`

---

## 8. Git e Higiene (Lean 5S)

- **Control Git**: No Push / No Merge. Commits atómicos y descriptivos. Verificar rama siempre.
- **Lean 5S**: No crear archivos basura (`test_*.md`, `scratch/` en raíz, etc.). Limpiar reportes temporales tras validación.

---

## 9. Cuándo detenerse (Stop Protocol)

Detenerse y pedir revisión humana si:
1. Hay contradicción entre documentos de `docs_control/`.
2. Un script de validación falla por falta de datos estratégicos.
3. Se solicita un cambio que rompe las **Reglas Críticas Sistreg** (ver README).
4. Se propone un cambio en la identidad comercial básica.

---

> [!NOTE]
> Este documento es la "Constitución" operativa. Ignorar estas reglas se considera un fallo crítico de calidad.
