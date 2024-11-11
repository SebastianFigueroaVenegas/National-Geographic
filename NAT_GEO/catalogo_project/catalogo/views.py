from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie, ChatMessage
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('catalog_view')  
        else:
            messages.error(request, "Credenciales incorrectas.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index') 

@login_required
def catalog_view(request):
    movies = Movie.objects.all()  
    return render(request, 'catalog.html', {'movies': movies})

@login_required
def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        ChatMessage.objects.create(sender=request.user, message=message)

        return HttpResponseRedirect(reverse('chat')) 
    
    messages = ChatMessage.objects.all()  
    return render(request, 'chat.html', {'messages': messages})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})





#############################################################################################################################


def verIndexHome(request):
    return render(request,'index_home.html')

def pelicula_detail(request, id):
    pelicula = get_object_or_404(Movie, id=id)
    return render(request, "peliculas_details.html", {'pelicula': pelicula})


###############################################################################################################################


