from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    # Página principal con el botón hacia familiares
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página Principal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007bff; /* Azul similar al del admin */
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenido a la página principal</h1>
        <p>Haz clic en el botón para ver la lista de familiares.</p>
        <a href="/familiares/">
            <button>Ver lista de familiares</button>
        </a>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home, name='home'),  # Ruta para la raíz
    path('admin/', admin.site.urls),  # Ruta para el admin
    path('familiares/', include('familiares.urls')),  # Ruta para la app familiares
    path('accounts/', include('django.contrib.auth.urls')),  # Sistema de autenticación de Django
]
