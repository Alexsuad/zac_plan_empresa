# Inventario de anexos y gráficos — Sistreg

Este documento es el control maestro para asegurar que el Plan de Empresa final cuenta con todo el soporte documental y visual necesario.

## 1. Anexos Documentales

| Código | Anexo | Fuente de Datos | Estado | Responsable | Automatizable |
|---|---|---|---|---|---|
| **A01** | CV Resumido Promotor | docs_convierte/equipo | Pendiente | Humano (Privacidad) | No |
| **A02** | CV Colaboración Externa | docs_convierte/equipo | Pendiente | Humano (Privacidad) | No |
| **A03** | Informe Investigación Mercado | docs_convierte/investigaciones | Disponible | IA (Auditoría) | Parcial (Rutas) |
| **A04** | Registro Naming Sistreg | 06_0_marca_comunicacion.md | Pendiente | Humano | No |
| **A05** | Soporte Metodológico Red ARCE | Google Sheets / Docs | Disponible | IA | No |

## 2. Gráficos Financieros (Cuantitativos)

*Deben ser generados por Python o extraídos directamente de la fuente numérica para evitar discrepancias.*

| Código | Gráfico | Fuente Numérica | Estado | Salida Esperada | Automatizable |
|---|---|---|---|---|---|
| **G01** | Inversión Inicial | Google Sheets (Pestaña Inversión) | Pendiente | `_build/graficos/g01_inversion.png` | Sí |
| **G02** | Estructura Costes Fijos | Google Sheets (Pestaña Gastos) | Pendiente | `_build/graficos/g02_costes_fijos.png` | Sí |
| **G03** | Previsión Ventas (Año 1-3) | Google Sheets (Pestaña Ventas) | Pendiente | `_build/graficos/g03_prevision_ventas.png` | Sí |
| **G04** | Punto de Equilibrio | Google Sheets (Pestaña Umbral) | Pendiente | `_build/graficos/g04_punto_equilibrio.png` | Sí |
| **G05** | Flujo de Tesorería | Google Sheets (Pestaña Caja) | Pendiente | `_build/graficos/g05_tesoreria.png` | Sí |

## 3. Gráficos Conceptuales (Estratégicos)

*Pueden ser diagramas Mermaid o diseños visuales propuestos por IA/Humano.*

| Código | Gráfico / Diagrama | Fuente Narrativa | Estado | Responsable | Automatizable |
|---|---|---|---|---|---|
| **C01** | Modelo Operativo Sistreg | 06_2_operaciones.md | Pendiente | IA + Humano | No (Mermaid) |
| **C02** | Flujo de Servicio (Embudo) | 06_1_marketing_ventas.md | Pendiente | IA + Humano | No (Mermaid) |
| **C03** | Mapa de Alianzas Zaragoza Activa / CONVIERTE | 03_1_analisis_externo.md | Pendiente | IA | No |
| **C04** | Cronograma de Implantación | 07_implantacion.md | Pendiente | Humano + IA | Parcial (Gantt) |

## 4. Reglas de Gestión de Gráficos
- **Ubicación de Salida:** Todos los gráficos generados deben vivir en `_build/graficos/`.
- **Nomenclatura:** Mantener el código (Gxx o Cxx) para facilitar las referencias en el texto.
- **Sincronización:** Si cambia el Google Sheets, se deben regenerar los gráficos de tipo G.
- **Consistencia:** Un gráfico G nunca debe entrar al documento final si no ha sido validado contra su fuente numérica.
- **Mapa de calor:** Mapa de calor de anexos (visualización del estado del Gate 2 de Zaragoza Activa / CONVIERTE).
