import os
import re
import sys

def audit_plan():
    respuestas_dir = 'respuestas_plan_empresa/'
    gates_file = 'docs_control/gates_entrega_sistreg.md'
    build_file = '_build/plan_empresa_sistreg_completo.md'
    entrega_anexos_dir = '_build/entrega/anexos/'

    if not os.path.exists(respuestas_dir):
        print(f"FAIL: Directorio {respuestas_dir} no existe.")
        return False

    all_files_clean = True
    pending_files = []
    
    block_patterns = [
        r'Pendiente de completar', 
        r'\[PENDIENTE\]', 
        r'\[CIFRA\]', 
        r'\[NÚMERO\]',
        r'TEST_01',
        r'TEST_02',
        r'test_externo'
    ]

    files = [f for f in os.listdir(respuestas_dir) if f.endswith('.md')]
    
    if len(files) == 0:
        print("FAIL: No hay archivos en respuestas_plan_empresa/")
        return False

    # 1. Check for blocking patterns
    for f in files:
        filepath = os.path.join(respuestas_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            for pat in block_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    pending_files.append(f)
                    all_files_clean = False
                    break # Stop at first block in this file
    
    # Remove duplicates from pending_files
    pending_files = list(set(pending_files))

    # 2. Check gates for false advances
    if os.path.exists(gates_file):
        with open(gates_file, 'r', encoding='utf-8') as gf:
            gates_content = gf.read()
        
        blocks = re.split(r'## Gate', gates_content)[1:]
        for block in blocks:
            lines = block.strip().split('\n')
            gate_name = lines[0].strip()
            
            estado = None
            files_in_gate = []
            
            for line in lines:
                if line.startswith('**Estado:**'):
                    estado = line.replace('**Estado:**', '').strip()
                match = re.search(r'`respuestas_plan_empresa/([^`]+)`', line)
                if match:
                    files_in_gate.append(match.group(1))
            
            if estado and 'Completado' in estado:
                for f in files_in_gate:
                    if f in pending_files:
                        print(f"FAIL: Avance falso detectado en Gate {gate_name}. El archivo {f} está marcado como Completado pero contiene marcadores bloqueantes.")
                        return False

    # 3. Check for premature build files
    if os.path.exists(build_file) and not all_files_clean:
        print(f"FAIL: El archivo {build_file} existe pero hay apartados pendientes ({len(pending_files)} archivos con marcadores).")
        return False

    # 4. Check for test files in entrega
    if os.path.exists(entrega_anexos_dir):
        test_files = [f for f in os.listdir(entrega_anexos_dir) if 'test' in f.lower() or f == 'test_externo.txt']
        if test_files:
            print(f"FAIL: Archivos de prueba detectados en salida final: {test_files}")
            return False

    if not all_files_clean:
        print(f"INFO: Hay {len(pending_files)} archivos pendientes o con artefactos de prueba: {', '.join(pending_files)}")
        print("FAIL: El plan de empresa no está completo.")
        return False

    print("PASS: El plan de empresa está completo, limpio de pruebas y no hay inconsistencias en los gates.")
    return True

if __name__ == '__main__':
    success = audit_plan()
    if not success:
        sys.exit(1)
    sys.exit(0)
