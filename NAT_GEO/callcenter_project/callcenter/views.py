from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AdminAction
from .api_client import API_BASE_URL, get_movies, create_movie, get_chat_messages, create_chat_message
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:  # Verifica si el usuario es administrador
            login(request, user)
            return redirect('manage_catalog')  # Redirige a la página de administración
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos o permisos insuficientes.")
    return render(request, 'login.html')

def admin_logout_view(request):
    logout(request)
    return redirect('admin_login')  # Redirige a la página de login del administrador

@login_required
def manage_catalog_view(request):
    # Obtiene todas las películas usando la API
    movies = get_movies()
    return render(request, 'manage_catalog.html', {'movies': movies})

@login_required
def create_movie_view(request):
    if request.method == 'POST':
        sucursal = request.POST['sucursal']
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        clasificacion = request.POST['clasificacion']
        duracion = request.POST['duracion']
        resena = request.POST['resena']
        sala = request.POST['sala']
        fecha_exhibicion = request.POST['fecha_exhibicion']
        hora_exhibicion = request.POST['hora_exhibicion']
        valor_ticket = request.POST['valor_ticket']
        imagen = request.FILES['imagen']

        
        response = create_movie({
            'sucursal': sucursal,
            'nombre': nombre,
            'genero': genero,
            'clasificacion': clasificacion,
            'duracion': duracion,
            'resena': resena,
            'sala': sala,
            'fecha_exhibicion': fecha_exhibicion,
            'hora_exhibicion': hora_exhibicion,
            'valor_ticket': valor_ticket,
        }, files={'imagen': imagen})

        if response.status_code == 201:
            movie_id = response.json().get('id')
            AdminAction.objects.create(admin=request.user, movie_id=movie_id)
            return redirect('manage_catalog')

    return render(request, 'movie_form.html')

@login_required
def edit_movie_view(request, movie_id):
    # Obtiene la película mediante la API
    response = requests.get(f'{API_BASE_URL}movies/{movie_id}/')
    movie = response.json() if response.status_code == 200 else None
    if request.method == 'POST':
        sucursal = request.POST['sucursal']
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        clasificacion = request.POST['clasificacion']
        duracion = request.POST['duracion']
        resena = request.POST['resena']
        sala = request.POST['sala']
        fecha_exhibicion = request.POST['fecha_exhibicion']
        hora_exhibicion = request.POST['hora_exhibicion']
        valor_ticket = request.POST['valor_ticket']
        imagen = request.POST['imagen']
        
        # Llama a la API para actualizar la película
        response = requests.put(f'{API_BASE_URL}movies/{movie_id}/', data={
            'sucursal': sucursal,
            'nombre': nombre,
            'genero': genero,
            'clasificacion': clasificacion,
            'duracion': duracion,
            'resena': resena,
            'sala': sala,
            'fecha_exhibicion': fecha_exhibicion,
            'hora_exhibicion': hora_exhibicion,
            'valor_ticket': valor_ticket,
            'imagen': imagen 
        })
        
        if response.status_code == 200:
            AdminAction.objects.create(admin=request.user, movie_id=movie_id)
            return redirect('manage_catalog')

    return render(request, 'movie_form.html', {'movie': movie})

@login_required
def delete_movie_view(request, movie_id):
    # Llama a la API para eliminar la película
    response = requests.delete(f'{API_BASE_URL}movies/{movie_id}/')
    
    if response.status_code == 204:
        AdminAction.objects.create(admin=request.user, movie_id=movie_id)
    
    return redirect('manage_catalog')

@login_required
def admin_chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        create_chat_message(message, request.user.id, is_admin=True)
        return HttpResponseRedirect(reverse('admin_chat'))
    
    # Obtiene todos los mensajes de chat usando la API
    messages = get_chat_messages()
    return render(request, 'chat.html', {'messages': messages})

