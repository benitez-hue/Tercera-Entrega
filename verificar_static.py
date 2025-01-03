import os

# Ruta de la carpeta estática
static_dir = os.path.join(os.path.dirname(__file__), 'static')

# Verificar y crear la carpeta si no existe
if os.path.exists(static_dir):
    print(f"La carpeta 'static/' ya existe en: {static_dir}")
else:
    os.makedirs(static_dir)
    print(f"Carpeta 'static/' creada en: {static_dir}")
