from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Aula(models.Model):
	NoAula			= models.IntegerField(primary_key = True) 
	Edificio		= models.IntegerField()

	def __str__(self):
		retorno = "Aula: %s   Edificio: %s"%(self.NoAula, self.Edificio)
		return retorno


class Materia(models.Model):
	IdMateria 		= models.CharField(primary_key = True, max_length = 15)
	Semestre		= models.IntegerField()
	Nombre			= models.CharField(max_length = 50)

	def __str__(self):
		retorno = "%s    %s"%(self.IdMateria, self.Nombre)
		return retorno

class Docente(models.Model):
	IdDocente		= models.IntegerField(primary_key = True)
	Nombre 			= models.CharField(max_length = 100)
	Materias 		= models.ManyToManyField(Materia)

	def __str__(self):
		return self.Nombre


class Clase(models.Model):
	IdClase 		= models.IntegerField(primary_key = True, unique = True)
	Materia			= models.ForeignKey(Materia, null = True, on_delete= models.CASCADE)	
	Aula			= models.ForeignKey(Aula, null = True, blank = True, on_delete= models.CASCADE)	
	Docente 		= models.ForeignKey(Docente, on_delete= models.CASCADE)
	Hora			= models.CharField(max_length = 15)
	Contador		= models.IntegerField()

	def __str__(self):
		retorno = "%s    %s    %s"%(self.IdClase, self.Materia.Nombre, self.Hora)
		return retorno

class Alumno(models.Model):
	NoControl		= models.IntegerField(primary_key = True, unique = True)
	Usuario			= models.OneToOneField(User,  on_delete=models.CASCADE)
	Nombre			= models.CharField(max_length = 100)
	Semestre 		= models.IntegerField()
	Materias 		= models.ManyToManyField(Materia, null = True, blank = True,)
	Clases	 		= models.ManyToManyField(Clase, null = True,blank = True,)


	def __str__(self):
		retorno = "%s    %s    %s"%(self.NoControl,self.Nombre, self.Usuario.username)
		return retorno