# Anexos del Plan de Empresa Sistreg

Este directorio contiene todos los anexos que se adjuntarán al documento principal.
La inclusión y formato de cada anexo se rigen estrictamente por el archivo `manifest_anexos.yml`.

## Reglas de gestión
- **Fuente de verdad:** Solo lo declarado en `manifest_anexos.yml` entra en la compilación final.
- **Anexos internos (`incluir_en_documento: true`):** Se insertarán como texto Markdown o gráficos en el documento consolidado.
- **Anexos externos (`incluir_en_documento: false`):** Se copiarán a la carpeta de entrega y se listarán en una tabla de referencias en el documento final.
- **Tipos soportados:** Markdown (`.md`), imágenes (`.png`, `.jpg`), PDFs y hojas de cálculo (`.xlsx`).
