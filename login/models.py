from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    cpf = models.CharField(max_length=40, unique=True)
    nome = models.CharField(max_length=40, blank=True, null=True)
    endereco = models.CharField(max_length=40, blank=True, null=True)
    telefone = models.CharField(max_length=40, blank=True, null=True)
