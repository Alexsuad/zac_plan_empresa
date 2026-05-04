# Arquitectura de Anexos y Tecnologías — ZAC

Este documento define los formatos y la estructura de los anexos para el Plan de Empresa ZAC.

## Tecnologías por tipo de contenido

- **Markdown (.md)**: Para documentos de texto estratégico y matrices narrativas.
  - DAFO, CAME, PESTEL, Canvas, Propuesta de Valor, Cliente Ideal, Matriz de Riesgos, Fuentes Consultadas, Glosario.
- **CSV (.csv)**: Para datos tabulares, comparativas de mercado y listados extensos.
  - Benchmark de competencia, Tabla Producto/Precio, Curva de Valor.
- **XLSX (.xlsx)**: Para toda la lógica financiera y numérica compleja.
  - Plan económico-financiero, Tesorería, Cuenta de Resultados, Balance, Punto de Equilibrio, Análisis de Escenarios.
- **Mermaid**: Para visualizaciones integradas en Markdown.
  - Organigrama, Flujo Operativo, Calendario Gantt, Flujo Comercial.
- **Python (.py)**: Para automatización de tareas y generación de evidencia.
  - Generación de gráficos, Consolidación de documentos, Validación de estructura.
- **DOCX/PDF**: Formatos exclusivos para la entrega final al cliente.
- **HTML**: No se utiliza en este repositorio por ahora.

## Estructura de la carpeta anexos/

```text
anexos/
├── A01_canvas_modelo_negocio.md
├── A02_propuesta_valor.md
├── A03_cliente_ideal.md
├── A04_pestel.md
├── A05_benchmark_competencia.md
├── A06_dafo.md
├── A07_came.md
├── A08_tabla_producto_precio.md
├── A09_plan_economico_financiero.md
├── A10_calendario_implantacion.md
├── A11_matriz_riesgos.md
├── A12_fuentes_consultadas.md
├── datos/        # Archivos CSV de soporte
├── finanzas/     # Archivos Excel (XLSX)
└── graficos/     # Salidas de scripts de Python
```
