from django.urls import path
from . import views

# Definición de las rutas de la aplicación familiares
urlpatterns = [
    # Ruta para la página principal de la app familiares
    path('index/', views.index, name='index'),  # Página principal con redirección al índice

    # Rutas para la funcionalidad de familiares
    path('', views.lista_familiares, name='lista_familiares'),  # Página principal para listar familiares
    path('agregar/', views.agregar_familiar, name='agregar_familiar'),  # Agregar un nuevo familiar
    path('editar/<int:pk>/', views.editar_familiar, name='editar_familiar'),  # Editar los datos de un familiar
    path('eliminar/<int:pk>/', views.eliminar_familiar, name='eliminar_familiar'),  # Eliminar un familiar existente

    # Rutas para la funcionalidad de amigos
    path('amigos/', views.lista_amigos, name='lista_amigos'),  # Página para listar amigos

    # Rutas para la funcionalidad de trabajos
    path('trabajos/', views.lista_trabajos, name='lista_trabajos'),  # Página para listar trabajos

    # Rutas para la funcionalidad de blogs
    path('blogs/', views.lista_blogs, name='lista_blogs'),  # Página para listar blogs
]
