Documentación del Proyecto
Objetivo
El objetivo del proyecto es crear una página web que muestre una lista de familiares con sus datos personales: nombre, edad y fecha de nacimiento.

Arquitectura del Proyecto
Modelos (models.py)
Define el modelo Familiar con los campos:

nombre: Nombre del familiar.
edad: Edad del familiar.
fecha_nacimiento: Fecha de nacimiento del familiar.
Vistas (views.py)
La vista lista_familiares consulta todos los datos almacenados en el modelo Familiar y los pasa a la plantilla para mostrarlos.

URLs (urls.py)
Se define la ruta /familiares/ que conecta la vista lista_familiares.

Plantillas (templates/lista_familiares.html)
Muestra en formato HTML la lista de familiares.

Admin Panel
Permite gestionar la información de familiares directamente desde la interfaz de administración de Django.

Pasos Realizados
Crear el Proyecto y Aplicación

Se creó el proyecto con django-admin startproject.
Se creó la aplicación familiares con python manage.py startapp.
Configurar el Modelo

En models.py se definió el modelo Familiar.
Se aplicaron las migraciones con:
bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Registrar el Modelo en el Admin

En admin.py se registró el modelo Familiar para gestionarlo desde el panel de administración.
Crear la Vista y URL

En views.py se agregó la lógica para consultar los datos de Familiar.
En urls.py se definió la ruta /familiares/.
Diseñar la Plantilla

En templates/lista_familiares.html se mostró la lista de familiares con un bucle de Django.
Instrucciones de Uso
Accede al panel de administración: http://127.0.0.1:8000/admin/.
Agrega datos de familiares desde el panel de administración.
Accede a la página de familiares: http://127.0.0.1:8000/familiares/.
Accede a la página de familiares: http://127.0.0.1:8000/familiares/lista/.
