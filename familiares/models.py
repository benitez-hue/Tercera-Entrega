from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from datetime import date

# ====================
# Clase Familiar
# ====================
class Familiar(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre completo",
        help_text="Ingrese el nombre completo del familiar."
    )
    edad = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        verbose_name="Edad",
        help_text="Ingrese la edad del familiar (de 0 a 120 años)."
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de nacimiento",
        help_text="Ingrese la fecha de nacimiento del familiar."
    )

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

    class Meta:
        verbose_name_plural = "Familiares"
        ordering = ['nombre']

# ====================
# Clase Amigo
# ====================
class Amigo(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre",
        help_text="Ingrese el nombre completo del amigo."
    )
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', "El número de teléfono debe tener entre 9 y 15 dígitos.")],
        verbose_name="Teléfono",
        help_text="Ingrese el número de teléfono del amigo (incluyendo código de país si es necesario)."
    )
    email = models.EmailField(
        verbose_name="Correo electrónico",
        help_text="Ingrese una dirección de correo electrónico válida."
    )
    familiar = models.ForeignKey(
        Familiar,
        on_delete=models.CASCADE,
        related_name='amigos',
        null=True,
        blank=True,
        verbose_name="Familiar relacionado",
        help_text="Seleccione un familiar relacionado, si aplica."
    )

    def __str__(self):
        return f"{self.nombre} ({self.telefono})"

    class Meta:
        verbose_name_plural = "Amigos"
        ordering = ['nombre']

# ====================
# Clase Trabajo
# ====================
class Trabajo(models.Model):
    nombre_empresa = models.CharField(
        max_length=100,
        verbose_name="Nombre de la empresa",
        help_text="Ingrese el nombre de la empresa."
    )
    posicion = models.CharField(
        max_length=50,
        verbose_name="Posición o cargo",
        help_text="Ingrese el cargo o posición desempeñada."
    )
    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Salario",
        help_text="Ingrese el salario asociado al trabajo."
    )
    descripcion = models.TextField(
        verbose_name="Descripción",
        help_text="Ingrese una descripción del trabajo."
    )

    def __str__(self):
        return f"{self.nombre_empresa} - {self.posicion}"

    class Meta:
        verbose_name_plural = "Trabajos"
        ordering = ['nombre_empresa']
        constraints = [
            models.UniqueConstraint(fields=['nombre_empresa', 'posicion'], name='unique_empresa_posicion')
        ]

# ====================
# Clase Blog
# ====================
class Blog(models.Model):
    def upload_to(instance, filename):
        return f'blog_images/{instance.autor.username}/{filename}'

    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Ingrese el título del blog."
    )
    subtitulo = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Subtítulo",
        help_text="Ingrese un subtítulo para el blog (opcional)."
    )
    cuerpo = models.TextField(
        verbose_name="Contenido",
        help_text="Ingrese el contenido del blog."
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Autor",
        help_text="Seleccione el autor del blog."
    )
    fecha = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de publicación"
    )
    imagen = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        verbose_name="Imagen asociada",
        help_text="Suba una imagen relacionada con el blog (opcional)."
    )

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.subtitulo:
            self.subtitulo = "Sin subtítulo"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ['-fecha']
