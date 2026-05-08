# Workflow: Validar Entrega Final

**Objetivo:** Verificar la integridad comercial y estratégica del documento final ensamblado, usando las skills agénticas pertinentes, para garantizar su aptitud frente al panel de Zaragoza Activa / CONVIERTE.

## Condiciones de Entrada
- El archivo consolidado `_build/plan_empresa_sistreg_completo.md` debe existir y haber sido generado limpiamente.

## Fases de ejecución

1. **Auditoría IA / Antigravity:**
   El agente aplica la skill `skill-auditoria-final` al archivo compilado.
   
2. **Revisión de Lenguaje Comercial:**
   El agente usa `skill-lenguaje-comercial-sistreg` para confirmar que el vocabulario respeta la propuesta de valor táctica (Doc-to-Cash, B2B logístico) sin alucinar beneficios inalcanzables.

3. **Confirmación de Gate de Entrega:**
   Si la revisión es exitosa, se marca formalmente en los documentos de control que el plan de empresa está listo para exportación en formatos de entrega, notificando al promotor con el dictamen final.
