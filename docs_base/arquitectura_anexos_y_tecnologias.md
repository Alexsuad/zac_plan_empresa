# Arquitectura de Anexos y Tecnologías — Sistreg

> [!IMPORTANT]
> Este documento define la arquitectura conceptual de anexos y tecnologías. La estructura operativa vigente de anexos se encuentra alineada con la carpeta `/anexos/` y con el mapa maestro `docs_base/02_mapa_transversal_anexos_investigaciones_validaciones.md`.

Este documento define los formatos y la estructura de los anexos para el Plan de Empresa de Sistreg.

## Tecnologías por tipo de contenido

- **Markdown (.md)**: Para texto estructurado, matrices estratégicas (DAFO, PESTEL) y narrativa técnica.
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

## Estructura operativa de la carpeta anexos/

```text
anexos/
├── A01_fuentes_sector_logistico.md
├── A02_competencia.md
├── A03_validaciones_clientes.md
├── A04_glosario_logistico.md
├── A05_tablas_financieras.md
├── datos/        # Archivos CSV de soporte (pendientes)
├── finanzas/     # Archivos Excel (XLSX) (pendientes)
└── graficos/     # Salidas de scripts de Python (pendientes)
```
