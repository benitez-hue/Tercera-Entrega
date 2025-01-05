from django.urls import path
from . import views

urlpatterns = [
    # Página principal de familiares
    path('', views.lista_familiares, name='lista_familiares'),

    # CRUD para Familiares
    path('agregar/', views.agregar_familiar, name='agregar_familiar'),
    path('editar/<int:pk>/', views.editar_familiar, name='editar_familiar'),
    path('eliminar/<int:pk>/', views.eliminar_familiar, name='eliminar_familiar'),

    # CRUD para Amigos
    path('amigos/', views.lista_amigos, name='lista_amigos'),
    path('amigos/agregar/', views.agregar_amigo, name='agregar_amigo'),
    path('amigos/editar/<int:pk>/', views.editar_amigo, name='editar_amigo'),
    path('amigos/eliminar/<int:pk>/', views.eliminar_amigo, name='eliminar_amigo'),

    # CRUD para Trabajos
    path('trabajos/', views.lista_trabajos, name='lista_trabajos'),
    path('trabajos/agregar/', views.agregar_trabajo, name='agregar_trabajo'),
    path('trabajos/editar/<int:pk>/', views.editar_trabajo, name='editar_trabajo'),
    path('trabajos/eliminar/<int:pk>/', views.eliminar_trabajo, name='eliminar_trabajo'),

    # CRUD para Blogs y Detalle
    path('blogs/', views.lista_blogs, name='lista_blogs'),
    path('blogs/agregar/', views.agregar_blog, name='agregar_blog'),
    path('blogs/editar/<int:pk>/', views.editar_blog, name='editar_blog'),
    path('blogs/eliminar/<int:pk>/', views.eliminar_blog, name='eliminar_blog'),
    path('blogs/detalle/<int:pk>/', views.detalle_blog, name='detalle_blog'),
]
