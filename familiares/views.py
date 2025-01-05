from django.shortcuts import render, get_object_or_404, redirect
from .models import Familiar, Amigo, Trabajo, Blog
from .forms import FamiliarForm, AmigoForm, TrabajoForm, BlogForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ====================
# VISTA PARA LA PÁGINA PRINCIPAL
# ====================
def index(request):
    return render(request, 'familiares/index.html')

# ====================
# VISTA PARA REGISTRO DE USUARIOS (SIGNUP)
# ====================
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# ====================
# VISTAS PARA FAMILIARES (CRUD COMPLETO)
# ====================
@login_required
def lista_familiares(request):
    familiares = Familiar.objects.all().order_by('nombre')
    paginator = Paginator(familiares, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_familiares.html', {'page_obj': page_obj})

@login_required
def agregar_familiar(request):
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
    familiar = get_object_or_404(Familiar, pk=pk)
    if request.method == 'POST':
        familiar.delete()
        return redirect('lista_familiares')
    return render(request, 'familiares/eliminar_familiar.html', {'familiar': familiar})

# ====================
# VISTAS PARA AMIGOS (CRUD COMPLETO)
# ====================
@login_required
def lista_amigos(request):
    amigos = Amigo.objects.all().order_by('nombre')
    paginator = Paginator(amigos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_amigos.html', {'page_obj': page_obj})

@login_required
def agregar_amigo(request):
    if request.method == 'POST':
        form = AmigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_amigos')
    else:
        form = AmigoForm()
    return render(request, 'familiares/agregar_amigo.html', {'form': form})

@login_required
def editar_amigo(request, pk):
    amigo = get_object_or_404(Amigo, pk=pk)
    if request.method == 'POST':
        form = AmigoForm(request.POST, instance=amigo)
        if form.is_valid():
            form.save()
            return redirect('lista_amigos')
    else:
        form = AmigoForm(instance=amigo)
    return render(request, 'familiares/editar_amigo.html', {'form': form})

@login_required
def eliminar_amigo(request, pk):
    amigo = get_object_or_404(Amigo, pk=pk)
    if request.method == 'POST':
        amigo.delete()
        return redirect('lista_amigos')
    return render(request, 'familiares/eliminar_amigo.html', {'amigo': amigo})

# ====================
# VISTAS PARA TRABAJOS (CRUD COMPLETO)
# ====================
@login_required
def lista_trabajos(request):
    trabajos = Trabajo.objects.all().order_by('nombre_empresa')
    paginator = Paginator(trabajos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_trabajos.html', {'page_obj': page_obj})

@login_required
def agregar_trabajo(request):
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_trabajos')
    else:
        form = TrabajoForm()
    return render(request, 'familiares/agregar_trabajo.html', {'form': form})

@login_required
def editar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == 'POST':
        form = TrabajoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('lista_trabajos')
    else:
        form = TrabajoForm(instance=trabajo)
    return render(request, 'familiares/editar_trabajo.html', {'form': form})

@login_required
def eliminar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    if request.method == 'POST':
        trabajo.delete()
        return redirect('lista_trabajos')
    return render(request, 'familiares/eliminar_trabajo.html', {'trabajo': trabajo})

# ====================
# VISTAS PARA BLOGS (CRUD Y DETALLE)
# ====================
@login_required
def lista_blogs(request):
    blogs = Blog.objects.all().order_by('-fecha')
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'familiares/lista_blogs.html', {'page_obj': page_obj})

@login_required
def detalle_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'familiares/detalle_blog.html', {'blog': blog})

@login_required
def agregar_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_blogs')
    else:
        form = BlogForm()
    return render(request, 'familiares/agregar_blog.html', {'form': form})

@login_required
def editar_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('lista_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'familiares/editar_blog.html', {'form': form})

@login_required
def eliminar_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('lista_blogs')
    return render(request, 'familiares/eliminar_blog.html', {'blog': blog})
