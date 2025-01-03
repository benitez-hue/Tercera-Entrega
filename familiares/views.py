from django.shortcuts import render, get_object_or_404, redirect
from .models import Familiar, Amigo, Trabajo, Blog
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import FamiliarForm  # Formularios necesarios para las vistas

# ====================
# VISTA PARA LA PÁGINA PRINCIPAL
# ====================

def index(request):
    """
    Vista de la página principal con un botón para redirigir a la lista de familiares.
    """
    return render(request, 'index.html')

# ====================
# VISTAS PARA FAMILIARES
# ====================

@login_required
def lista_familiares(request):
    """
    Vista para listar familiares con paginación.
    """
    familiares = Familiar.objects.all().order_by('nombre')  # Ordena por nombre
    paginator = Paginator(familiares, 10)  # Número de familiares por página
    page_number = request.GET.get('page')  # Obtiene la página actual de los parámetros GET
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_familiares.html', {'page_obj': page_obj})

@login_required
def agregar_familiar(request):
    """
    Vista para agregar un nuevo familiar.
    """
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_familiares')
    else:
        form = FamiliarForm()
    return render(request, 'familiares/agregar_familiar.html', {'form': form})

@login_required
def editar_familiar(request, pk):
    """
    Vista para editar los datos de un familiar.
    """
    familiar = get_object_or_404(Familiar, pk=pk)
    if request.method == 'POST':
        form = FamiliarForm(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
            return redirect('lista_familiares')
    else:
        form = FamiliarForm(instance=familiar)
    return render(request, 'familiares/editar_familiar.html', {'form': form})

@login_required
def eliminar_familiar(request, pk):
    """
    Vista para eliminar un familiar.
    """
    familiar = get_object_or_404(Familiar, pk=pk)
    if request.method == 'POST':
        familiar.delete()
        return redirect('lista_familiares')
    return render(request, 'familiares/eliminar_familiar.html', {'familiar': familiar})

# ====================
# VISTAS PARA AMIGOS
# ====================

@login_required
def lista_amigos(request):
    """
    Vista para listar amigos con paginación.
    """
    amigos = Amigo.objects.all().order_by('nombre')  # Ordena por nombre
    paginator = Paginator(amigos, 10)  # Número de amigos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_amigos.html', {'page_obj': page_obj})

# ====================
# VISTAS PARA TRABAJOS
# ====================

@login_required
def lista_trabajos(request):
    """
    Vista para listar trabajos con paginación.
    """
    trabajos = Trabajo.objects.all().order_by('nombre_empresa')  # Ordena por nombre de empresa
    paginator = Paginator(trabajos, 10)  # Número de trabajos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_trabajos.html', {'page_obj': page_obj})

# ====================
# VISTAS PARA BLOGS
# ====================

@login_required
def lista_blogs(request):
    """
    Vista para listar blogs con paginación.
    """
    blogs = Blog.objects.all().order_by('-fecha')  # Ordena por fecha descendente
    paginator = Paginator(blogs, 10)  # Número de blogs por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_blogs.html', {'page_obj': page_obj})
