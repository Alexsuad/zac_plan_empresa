# Plan de Implementación: Auditoría de Coherencia Textual Sistreg

**ID:** IP-AUDIT-01
**Estado:** Propuesta
**Versión:** 1.0

## 1. Alcance y Objetivos
Crear un script Python (`scripts/auditar_coherencia_textual.py`) que actúe como auditor determinista del repositorio. Su misión es detectar términos prohibidos, naming antiguo o promesas financieras arriesgadas sin realizar modificaciones automáticas.

## 2. Archivos a crear / modificar
- **Crear:** `scripts/auditar_coherencia_textual.py`
- **Crear:** `_build/reportes/` (Directorio de salida)
- **Modificar:** `.gitignore` (Para asegurar que los reportes de `_build/` no se versionen).

## 3. Lógica de Auditoría (Patrones)

### 3.1. Patrones de ERROR (Bloqueantes)
El script buscará coincidencias mediante Regex para:
- `Sistreg\s*/\s*Proyecto Logístico`: Prohibido el uso mixto.
- `Proyecto Logístico`: Error si NO va acompañado de "referencia interna", "descriptiva" o "ámbito de actuación".
- `\bZAC\b`: Error si NO va acompañado de "Zaragoza Activa", "CONVIERTE" o "contexto institucional".
- `piloto pagado` / `fase piloto`: Error si se presenta como oferta comercial.
- `diagnóstico y análisis` / `Horas de diagnóstico`: Terminología financiera obsoleta.
- `Sistreg es marca registrada`: Afirmación legal falsa.
- `ayudas concedidas` / `subvención segura`: Promesas de financiación no verificadas.
- `ROI garantizado` / `ahorro garantizado` / `resultados garantizados`: Falta de prudencia financiera.

### 3.2. Excepciones de Uso Correcto (Lógica Negativa)
- Se permitirá `piloto pagado` solo si la línea contiene verbos de prohibición (`no usar`, `no debe`).
- Se permitirá `Proyecto Logístico` o `ZAC` si la misma línea contiene las etiquetas de aclaración definidas.

## 4. Criterios de Validación
- **PASS:** 0 errores detectados.
- **FAIL:** >= 1 error detectado. Bloquea la consolidación final.

## 5. Áreas de Inspección
| Incluir | Excluir |
|---|---|
| `README.md` | `docs_convierte/` |
| `AGENTS.md` | `_build/` |
| `docs_control/` | `.git/` |
| `respuestas_plan_empresa/` | `anexos/` |
| `.agent/skills/` | `__pycache__/` |

## 6. Salida Esperada (Entregable)
Un reporte en `_build/reportes/auditoria_coherencia_textual.md` con:
- Resumen ejecutivo (Total archivos, errores, advertencias).
- Tabla de hallazgos (Archivo, Línea, Patrón, Severidad, Motivo, Sugerencia).
- Resultado final (PASS/FAIL).

## 7. Riesgos y Mitigación
- **Riesgo:** Falsos positivos en frases explicativas. -> **Mitigación:** Ajuste de Regex y niveles de severidad.
- **Riesgo:** Problemas de encoding en Windows/WSL. -> **Mitigación:** Forzar UTF-8.

## 8. Estrategia de Prueba
1. **Prueba unitaria:** Ejecutar contra una carpeta de test con errores provocados.
2. **Validación de falsos positivos:** Verificar que las reglas de exclusión funcionan.
3. **Generación de reporte:** Comprobar formato Markdown.
