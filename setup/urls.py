from django.contrib import admin
from django.urls import include, path
from index.views import agendar, inicio, iniciar_sesion, home, registro, paciente, doctor, secretaria, reagendar, hora, lista_citas, agregar_cita, index

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login/', iniciar_sesion, name="login"),
    path('home/', home, name="home"),
    path('register/', registro, name="register"),
    path('agendar/', agendar, name="agendar"),
    path('paciente/', paciente, name="paciente"),
    path('doctor/', doctor, name="doctor"),
    path('secretaria/', secretaria, name="secretaria"),
    path('reagendar/', reagendar, name="reagendar"),
    path('hora/', hora, name="hora"),
    path('citas/', lista_citas, name='lista_citas'),
    path('agregar/', agregar_cita, name='agregar_cita'),
    path('inicio/', inicio, name="inicio")
   
]
