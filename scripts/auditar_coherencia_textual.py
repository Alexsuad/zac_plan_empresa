import os
import re
import datetime
from pathlib import Path

# Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent.parent
INSPECT_PATHS = [
    'README.md',
    'AGENTS.md',
    'docs_control/',
    'respuestas_plan_empresa/',
    '.agent/skills/'
]
EXCLUDE_PATHS = [
    'docs_convierte/',
    '_build/',
    '.git/',
    '__pycache__/',
    'anexos/',
    'scripts/',
    'docs_control/plan_implementacion_auditoria_coherencia.md'
]
OUTPUT_FILE = BASE_DIR / '_build' / 'reportes' / 'auditoria_coherencia_textual.md'

# Definición de Patrones y Lógica
PATTERNS = [
    {
        'id': 'P01',
        'name': 'Naming Mixto',
        'regex': r'Sistreg\s*/\s*Proyecto Logístico',
        'severity': 'ERROR',
        'reason': 'Prohibido el uso de marca mixta Sistreg / Proyecto Logístico.',
        'suggestion': 'Usar solo Sistreg (o Proyecto Logístico indicando que es referencia interna).'
    },
    {
        'id': 'P02',
        'name': 'Proyecto Logístico como Marca',
        'regex': r'Proyecto Logístico',
        'severity': 'ERROR',
        'reason': 'Proyecto Logístico detectado sin aclaración de referencia interna.',
        'exclude_if': r'referencia interna|descriptiva|ámbito de actuación|no es marca comercial',
        'suggestion': 'Añadir que es una referencia interna/descriptiva.'
    },
    {
        'id': 'P03',
        'name': 'ZAC como Nombre de Proyecto',
        'regex': r'\bZAC\b',
        'severity': 'ERROR',
        'reason': 'Uso de ZAC detectado sin contexto institucional.',
        'exclude_if': r'Zaragoza Activa|CONVIERTE|contexto institucional|programa',
        'suggestion': 'Clarificar contexto institucional (Zaragoza Activa / Programa CONVIERTE).'
    },
    {
        'id': 'P04',
        'name': 'Servicio Piloto Comercial',
        'regex': r'piloto pagado|fase piloto|piloto limitado',
        'severity': 'ERROR',
        'reason': 'Uso de "piloto" como servicio comercial.',
        'exclude_if': r'no usar|no debe|no se permite',
        'suggestion': 'Usar "arranque guiado" en su lugar.'
    },
    {
        'id': 'P05',
        'name': 'Servicios Obsoletos',
        'regex': r'diagnóstico y análisis|Horas de diagnóstico',
        'severity': 'ERROR',
        'reason': 'Terminología de servicios obsoleta detectada.',
        'suggestion': 'Usar "arranque guiado" o "diagnóstico gratuito".'
    },
    {
        'id': 'P06',
        'name': 'Afirmación Legal Falsa',
        'regex': r'Sistreg\s+es\s+marca\s+registrada',
        'severity': 'ERROR',
        'reason': 'Afirmación de marca registrada no válida.',
        'suggestion': 'Indicar que Sistreg es marca provisional.'
    },
    {
        'id': 'P07',
        'name': 'Falta de Prudencia Financiera',
        'regex': r'ayudas concedidas|subvención segura|ROI garantizado|ahorro garantizado|resultados garantizados',
        'severity': 'ERROR',
        'reason': 'Promesas de resultados o ayudas no verificadas.',
        'suggestion': 'Usar lenguaje prudente (ej: previsión, estimación, potencial).'
    }
]

def audit():
    os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
    results = []
    files_audited = 0
    errors = 0
    warnings = 0
    infos = 0

    print(f"Iniciando auditoría en {BASE_DIR}...")

    for path_str in INSPECT_PATHS:
        path = BASE_DIR / path_str
        if not path.exists():
            continue

        files = []
        if path.is_file():
            files = [path]
        else:
            files = list(path.rglob('*.md')) + list(path.rglob('*.SKILL')) + list(path.rglob('SKILL.md'))

        for file_path in files:
            # Exclusiones
            if any(exc in str(file_path) for exc in EXCLUDE_PATHS):
                continue

            files_audited += 1
            try:
                content = file_path.read_text(encoding='utf-8')
                lines = content.splitlines()
                
                for line_num, line in enumerate(lines, 1):
                    for p in PATTERNS:
                        if re.search(p['regex'], line):
                            # Verificar exclusiones del patrón
                            if 'exclude_if' in p and re.search(p['exclude_if'], line):
                                results.append({
                                    'file': str(file_path.relative_to(BASE_DIR)),
                                    'line': line_num,
                                    'pattern': p['name'],
                                    'severity': 'INFO',
                                    'reason': 'Uso permitido detectado.',
                                    'suggestion': '-'
                                })
                                infos += 1
                                continue
                            
                            # Registrar hallazgo
                            results.append({
                                'file': str(file_path.relative_to(BASE_DIR)),
                                'line': line_num,
                                'pattern': p['name'],
                                'severity': p['severity'],
                                'reason': p['reason'],
                                'suggestion': p['suggestion']
                            })
                            if p['severity'] == 'ERROR': errors += 1
                            elif p['severity'] == 'WARNING': warnings += 1

            except Exception as e:
                print(f"Error leyendo {file_path}: {e}")

    # Generar Reporte Markdown
    status = "PASS" if errors == 0 else "FAIL"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = [
        f"# Reporte de Auditoría de Coherencia Textual — Sistreg",
        f"\n**Fecha de ejecución:** {now}",
        f"\n## Resumen Ejecutivo",
        f"- **Estado Final:** {status}",
        f"- **Archivos revisados:** {files_audited}",
        f"- **Total Errores:** {errors}",
        f"- **Total Advertencias:** {warnings}",
        f"- **Total Info (Usos permitidos):** {infos}",
        f"\n## Detalle de Hallazgos",
        "\n| Archivo | Línea | Patrón | Severidad | Motivo | Sugerencia |",
        "|---|---|---|---|---|---|",
    ]

    for r in results:
        report.append(f"| {r['file']} | {r['line']} | {r['pattern']} | {r['severity']} | {r['reason']} | {r['suggestion']} |")

    OUTPUT_FILE.write_text("\n".join(report), encoding='utf-8')
    
    print("-" * 30)
    print(f"AUDITORÍA FINALIZADA: {status}")
    print(f"Errores: {errors}")
    print(f"Advertencias: {warnings}")
    print(f"Reporte generado en: {OUTPUT_FILE}")
    print("-" * 30)

if __name__ == "__main__":
    audit()
