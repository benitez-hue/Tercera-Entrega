from django import forms
from .models import Familiar, Amigo, Trabajo, Blog

# Formulario para Familiar
class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'edad', 'fecha_nacimiento']

# Formulario para Amigo
class AmigoForm(forms.ModelForm):
    class Meta:
        model = Amigo
        fields = ['nombre', 'telefono', 'email', 'familiar']

# Formulario para Trabajo
class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['nombre_empresa', 'posicion', 'salario']

# Formulario para Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']
