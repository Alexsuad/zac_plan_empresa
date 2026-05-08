import os
import glob

def replace_in_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(script_dir, '..', 'docs_base', 'legal')
    files = glob.glob(os.path.join(directory, '*.md'))
    count = 0
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'Proyecto_automatizaciones' in content:
            new_content = content.replace('Proyecto_automatizaciones', 'Proyecto Sistreg')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reemplazado en: {os.path.basename(file_path)}")
            count += 1
            
    print(f"Total archivos modificados: {count}")

if __name__ == '__main__':
    replace_in_files()
