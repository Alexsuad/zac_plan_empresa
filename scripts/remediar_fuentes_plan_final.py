# File: scripts/remediar_fuentes_plan_final.py
# Propósito: Saneamiento de restos finos (autoempleo, pilotos, cifras antiguas) en fuentes base.
# ──────────────────────────────────────────────────────────────────────

import os
import sys

# Mapeo de archivos y sus reemplazos específicos con patrones corregidos por inspección
REEMPLAZOS = {
    "respuestas_plan_empresa/03_3_analisis_interno.md": [
        (
            'El análisis interno de **Sistreg** permite valorar si el proyecto cuenta con las capacidades y recursos mínimos para transformar la oportunidad detectada en un negocio viable. La conclusión principal es que la iniciativa dispone de una base técnica y operativa excepcionalmente sólida para una estructura de autoempleo, fundamentada en la **hibridez del promotor**.',
            'El análisis interno de **Sistreg** permite valorar si el proyecto cuenta con las capacidades y recursos mínimos para transformar la oportunidad detectada en un negocio viable. La conclusión principal es que la iniciativa dispone de una base técnica y operativa sólida para una estructura empresarial ligera, fundamentada en la **hibridez del promotor**.'
        ),
        (
            '- **Tesorería de Seguridad:** El proyecto cuenta con una inversión inicial propia de **5.000 €**. Tras cubrir los gastos de lanzamiento (~3.110 €), se dispone de un margen de seguridad de 6 meses para validar el modelo de negocio. Esta prudencia financiera permite centrarse en la calidad de los primeros clientes sin la presión de un flujo de caja inmediato desesperado.',
            '- **Tesorería de seguridad:** El proyecto cuenta con una aportación inicial propia prevista de **9.278 €**. Tras cubrir los gastos de lanzamiento, se mantiene un margen de seguridad para validar el modelo de negocio sin recurrir a deuda bancaria inicial. Esta prudencia financiera permite centrarse en la calidad de los primeros clientes y en el control de costes durante la fase de validación.'
        ),
        (
            'La estrategia interna debe ser la de un "especialista quirúrgico": aprovechar la agilidad y la capacidad de decisión inmediata para detectar problemas muy específicos en clientes seleccionados de Zaragoza, demostrando que una estructura de autoempleo profesional puede ofrecer soluciones de control operativo más eficaces, cercanas y rentables que las consultoras generalistas.',
            'La estrategia interna debe ser la de un "especialista quirúrgico": aprovechar la agilidad y la capacidad de decisión inmediata para detectar problemas muy específicos en clientes seleccionados de Zaragoza, demostrando que una estructura empresarial ligera y especializada puede ofrecer soluciones de control operativo más eficaces, cercanas y rentables que las consultoras generalistas.'
        )
    ],
    "respuestas_plan_empresa/04_dafo_came.md": [
        (
            'ofrecer pilotos muy cercanos y personalizados',
            'ofrecer validaciones técnicas acotadas, cercanas y personalizadas'
        ),
        (
            'Documentar el primer proyecto piloto con métricas de "antes y después" de la intervención para generar credibilidad.',
            'Documentar el primer caso de validación con métricas de "antes y después" de la intervención para generar credibilidad.'
        )
    ],
    "respuestas_plan_empresa/03_2_estudio_mercado.md": [
        (
            'Para asegurar la viabilidad del proyecto como autoempleo, se ha dimensionado el mercado de forma realista:',
            'Para asegurar la viabilidad del proyecto como servicio B2B especializado, se ha dimensionado el mercado de forma realista:'
        ),
        (
            'Sistreg no se posiciona por precio, sino por **retorno de inversión (ROI)** y **facilidad de adopción**.',
            'Sistreg no se posiciona por precio, sino por **retorno potencial medible** y **facilidad de adopción**.'
        ),
        (
            'proporciona la base necesaria para iniciar una actividad de autoempleo sostenible y profesional',
            'proporciona la base necesaria para iniciar una actividad empresarial ligera, sostenible y profesionalizada'
        )
    ],
    "respuestas_plan_empresa/05_objetivos_lineas_estrategicas.md": [
        (
            'modelo de cobro (ROI)',
            'modelo de cobro y retorno potencial medible'
        )
    ],
    "respuestas_plan_empresa/00_resumen_ejecutivo.md": [
        (
            'Como contexto operativo, el proyecto se apoya en una iniciativa de autoempleo técnico especializado bajo un modelo de autónomo con colaboración externa puntual y flexible, lo que garantiza una gestión de recursos prudente y sostenible durante la fase de lanzamiento (ver **Capítulo 1**).',
            'Como contexto operativo, el proyecto se apoya en una estructura inicial de autónomo con colaboración externa, propia de una fase de validación empresarial prudente.'
        )
    ],
    "respuestas_plan_empresa/01_equipo_promotor.md": [
        (
            'Mi perfil se define por una integración de tres áreas de conocimiento que rara vez coinciden en una estructura de autoempleo, lo que constituye la principal ventaja competitiva de Sistreg:',
            'Mi perfil se define por una integración de tres áreas de conocimiento que rara vez coinciden en una estructura empresarial ligera, lo que constituye la principal ventaja competitiva de Sistreg:'
        )
    ]
}

def aplicar_remediacion():
    count = 0
    for ruta, pares in REEMPLAZOS.items():
        if not os.path.exists(ruta):
            print(f"SKIP: {ruta} no encontrado.")
            continue
            
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            
        original = contenido
        for buscar, reemplazar in pares:
            if buscar in contenido:
                contenido = contenido.replace(buscar, reemplazar)
                count += 1
            else:
                # Intento de búsqueda parcial para diagnóstico si falla
                print(f"WARNING: No se encontró patrón exacto en {ruta}")
        
        if original != contenido:
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            print(f"OK: {ruta} actualizado.")
            
    print(f"\nSaneamiento completado. Total de reemplazos: {count}")

if __name__ == "__main__":
    aplicar_remediacion()
