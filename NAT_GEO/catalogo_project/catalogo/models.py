from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Movie(models.Model):
    sucursal = models.CharField(max_length=255)
    nombre = models.TextField(max_length=255)
    genero = models.TextField(max_length=255)
    clasificacion = models.TextField(max_length=100)
    duracion = models.PositiveIntegerField()
    resena = models.TextField(max_length=255)
    sala = models.PositiveIntegerField()
    fecha_exhibicion = models.DateField()
    hora_exhibicion = models.TimeField()
    valor_ticket = models.PositiveIntegerField()
    imagen = models.ImageField()





class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
