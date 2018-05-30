#from patterns import patterns
from django.conf.urls import  include, url
from principal.views import MenuView, AlumnosView, DocentesView, MateriasView, IndexView

urlpatterns = [#patterns('',

 	url(r'^$' , 'django.contrib.auth.views.login', 
 		{IndexView.as_view()}, name = 'login' ),


 	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
         name= 'logout' ),


 	url(r'^accounts/profile/', MenuView.as_view(), name="menu"),


 	url(r'^Alumnos/', AlumnosView.as_view(), name = "alum"),
    url(r'^Docentes/', DocentesView.as_view(), name = "doc"),
    url(r'^Materias/', MateriasView.as_view(), name = "mat"),

]#)