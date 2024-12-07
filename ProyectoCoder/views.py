

from django.shortcuts import render

from django.template import Template, Context, loader

from django.http import HttpResponse

from AppCoder.models import Curso



def inicio(request):
    return render(request, 'Inicio.html')

def Cursos(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"],comision=request.POST["comision"])
        curso.save()
        return render(request, "Cursos.html")
    else:
        return render(request, "Cursos.html")

def cursos(request):
    cursos= Curso.objects.all()
    print(cursos)
    return render(request, "tabla.html", {"cursos":cursos})

def Estudiante(request):
    return render(request, 'Estudiante.html')

def Entregables(request):
    return render(request, 'Entregables.html')

def Profesor(request):
    return render(request, 'Profesor.html')