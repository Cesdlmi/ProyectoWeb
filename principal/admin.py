from django.contrib import admin

from .models import Alumno, Aula, Docente, Materia, Clase

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Aula)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Clase)

