from django import forms
from .models import Alumno



class AlumnoForm (forms.ModelForm):


	class Meta:
		model= Alumno

		fields = [
			'Materias',
			

		]

		labels={
			'Materias': 'Nombre Materia',
			

		}

		widgets = {
			'Materias': forms.CheckboxSelectMultiple(),
			
		}