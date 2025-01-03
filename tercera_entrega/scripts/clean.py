import os
import shutil

def clean_project():
    for root, dirs, files in os.walk("."):
        # Eliminar directorios __pycache__
        for dir in dirs:
            if dir == "__pycache__":
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path)
                print(f"Directorio eliminado: {dir_path}")
        # Eliminar archivos .pyc
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Archivo eliminado: {file_path}")

if __name__ == "__main__":
    clean_project()
    print("Limpieza de archivos .pyc y directorios __pycache__ completada.")
