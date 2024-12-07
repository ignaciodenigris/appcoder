from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100) 
    comision = models.IntegerField() 

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)  
    email = models.EmailField() 

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField()  # Campo de email
    profesion = models.CharField(max_length=50)  

class Entregable(models.Model):
    nombre = models.CharField(max_length=100) 
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField() 
