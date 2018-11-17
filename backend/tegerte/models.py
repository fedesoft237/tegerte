from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Acudiente(models.Model):
    nombre = models.CharField(max_length=200) 
    apellidos = models.CharField(max_length=200) 
    documento = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)
    direccion= models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return self.nombre

class Vusuario(models.Model): 
    nombre = models.CharField(max_length=200) 
    apellidos = models.CharField(max_length=200) 
    documento = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)
    direccion= models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    def __str__(self): 
        return self.nombre
    
class Entidad(models.Model):
    entidad = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200) 
    direccion= models.CharField(max_length=200) 
    telefono = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return self.entidad

class TipoSuceso(models.Model):
    tiposuceso = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.tiposuceso 

class Agresor(models.Model):
    nombre = models.CharField(max_length=200) 
    apellidos = models.CharField(max_length=200) 
    documento = models.CharField(max_length=20)
    telefono = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return self.nombre 

class Suceso(models.Model): 
    inicio = models.DateTimeField(auto_now_add=True) 
    ubicacion = models.CharField(max_length=200) 
    agresor = models.ForeignKey(Agresor, on_delete=models.CASCADE)
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE)
    tiposuceso = models.ForeignKey(TipoSuceso, on_delete=models.CASCADE)
    def __str__(self): 
        return self.ubicacion


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    perfil = models.TextField(max_length=500, blank=True)