# File: docs_control/politica_extension_plan_empresa.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Establecer la política oficial de extensión y linealidad.
# Rol: Referencia normativa para el Auditor de Linealidad.
# ──────────────────────────────────────────────────────────────────────

# Política de Extensión y Linealidad Documental - Sistreg

## 1. Objetivo
Garantizar que el Plan de Empresa de Sistreg sea un documento lineal, coherente y de extensión controlada, evitando la redundancia y el crecimiento excesivo de páginas.

## 2. Ratios de Medición
Para la estimación de extensión en el formato final, se aplican los siguientes ratios:
- **Ratio Principal:** 300 palabras por página (Estándar de calidad).
- **Ratio Conservador:** 250 palabras por página (Escenario de máxima densidad).

## 3. Límites de Extensión
- **Objetivo Ideal:** 50 páginas (Ratio principal).
- **Límite de Alerta Leve:** 60 páginas.
- **Límite de Alerta Fuerte:** 70 páginas.
- **Bloqueo de Entrega:** > 70 páginas.

## 4. Reglas de Linealidad
1. **Capítulo Único:** El plan se redacta como un único libro fragmentado en archivos. No se deben repetir introducciones al proyecto en cada capítulo.
2. **Referencia vs. Explicación:** Si un concepto ya ha sido definido en su "Sede de Información", el resto de archivos deben referenciarlo brevemente, no explicarlo de nuevo.
3. **Control de Conceptos Tácticos:** Conceptos como "Doc-to-Cash" tienen sedes específicas. Su uso fuera de sede debe ser mínimo y estrictamente necesario para el contexto del capítulo.
4. **Prohibición de Redundancia:** Se prohíbe el uso de párrafos idénticos o altamente similares (>88%) entre diferentes secciones del plan.

## 5. Auditoría y Gates
- La auditoría de linealidad es un paso obligatorio antes de cualquier compilación oficial.
- El estado `LINEALIDAD_FAIL` bloquea la generación de archivos para entrega.
- El estado `LINEALIDAD_WARNING` permite compilación de prueba pero requiere revisión manual antes de proceder.
