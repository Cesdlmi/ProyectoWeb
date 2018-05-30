from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from .models import Alumno, Materia, Docente, Clase
from django.db import models

from django.contrib.auth.models import User

from .forms import AlumnoForm

 #Create your views here.


class IndexView(TemplateView):

	template_name = 'index.html'


class MenuView(TemplateView):

	template_name = 'menu.html'
	#noControl = Alumno.objects.filter(usuario=)



class AlumnosView(TemplateView):
	template_name='alumnos.html'


class DocentesView(TemplateView):
	template_name='docente.html'


class MateriasView(TemplateView):
	template_name='materias.html'
	


def materias_list(request):
	materia= Materia.objects.all()
	contexto={'materias':materia}
	return render(request, 'materias.html', contexto)


def docentes_list(request):
	docente= Docente.objects.all()
	contexto={'docentes':docente}
	return render(request, 'docente.html', contexto)

def alumnos_View(request):
	#form= AlumnoForm()
	#return render(request, 'alumnos.html', {'form':form})

	alumno= Alumno.objects.get(Usuario = request.user)
	clases= Clase.objects.filter(Materia__Semestre=alumno.Semestre).order_by('Materia')
	tomadas= alumno.Clases.all().values_list('IdClase', flat=True)
	print(tomadas)
	contexto={'clases':clases, 'tomadas':tomadas}
	return render(request, 'alumnos.html', contexto)


def infoAlumno_View(request, *kwargs):
	alumno= Alumno.objects.filter(Usuario = request.user)
	contexto={'alumnos':alumno}
	return render(request, 'menu.html', contexto)

def eleccion(request):
	alumno= Alumno.objects.get(Usuario = request.user)
	alumno.Clases.clear()
	for clases in filter(lambda key:key.startswith('elec'), request.POST.keys()):
		clas = request.POST[clases]
		alumno.Clases.add(clas)

	conts = Clase.objects.all()
	for i in conts:
		i.Contador = i.alumno_set.count()
		i.save()

	return redirect("/Alumnos")