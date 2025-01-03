import os

# Ruta de la carpeta 'media'
media_dir = os.path.join(os.path.dirname(__file__), 'media')

# Verificar y crear la carpeta si no existe
if os.path.exists(media_dir):
    print(f"La carpeta 'media/' ya existe en: {media_dir}")
else:
    os.makedirs(media_dir)
    print(f"Carpeta 'media/' creada en: {media_dir}")
