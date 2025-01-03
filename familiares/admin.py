from django.contrib import admin
from .models import Familiar, Amigo, Trabajo

# Registrar modelos en el admin
admin.site.register(Familiar)
admin.site.register(Amigo)
admin.site.register(Trabajo)
