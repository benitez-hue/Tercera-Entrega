from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from familiares import views as familiares_views

# ====================
# VISTA PARA LA PÁGINA PRINCIPAL
# ====================
def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Página Principal</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                button { padding: 10px 20px; font-size: 16px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
                button:hover { background-color: #0056b3; }
            </style>
        </head>
        <body>
            <h1>Bienvenido a la página principal</h1>
            <p>Haz clic en uno de los botones para ver las listas.</p>
            <a href="/familiares/"><button>Ver lista de familiares</button></a>
            <a href="/familiares/amigos/"><button>Ver lista de amigos</button></a>
            <a href="/familiares/trabajos/"><button>Ver lista de trabajos</button></a>
            <a href="/familiares/blogs/"><button>Ver lista de blogs</button></a>
        </body>
        </html>
    """)

# ====================
# DEFINICIÓN DE RUTAS (URLS)
# ====================
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('familiares/', include('familiares.urls')),  # Incluye las rutas de la app 'familiares'
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', familiares_views.signup, name='signup'),
]
