from django.shortcuts import render, redirect
from .models import *
from .forms import LoginForm, RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Cita
from .forms import CitaForm
from datetime import datetime

def index(request):
    return render(request, 'index.html') 
def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Verificar si el usuario ya existe
            correo = form.cleaned_data['correo']
            rut = form.cleaned_data['rut']

            if User.objects.filter(email=correo).exists():
                messages.error(request, 'El usuario ya está creado.')
            elif User.objects.filter(username=rut).exists():
                messages.error(request, 'El RUT ya está en uso.')
            else:
                form.save()
                messages.success(request, 'El usuario ha sido registrado exitosamente.')
                return redirect('login')  # Reemplaza 'nombre_url' con la URL deseada después del registro exitoso
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                form.add_error(None, 'Credenciales inválidas') 
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def agendar(request):
    return render(request, 'agendar.html') 

def paciente(request):
    return render(request, 'paciente.html') 

def doctor(request):
    return render(request, 'doctor.html') 

def secretaria(request):
    return render(request, 'secretaria.html') 

def reagendar(request):
    return render(request, 'reagendar.html') 

def hora(request):
    return render(request, 'hora.html') 

def inicio(request):
    return render(request, 'inicio.html') 

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'lista_citas.html', {'citas': citas})


def agregar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            print(form.cleaned_data)
            cita.doctor = form.cleaned_data['doctor']
            fecha = form.cleaned_data['fecha']
            fecha_str = fecha.strftime('%Y-%m-%d')  # Convierte la fecha en una cadena en formato 'YYYY-MM-DD'
            fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d')  # Convierte la cadena de fecha en objeto datetime
            cita.fecha = fecha_dt
            cita.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'agregar_cita.html', {'form': form})


def lista_citas_view(request):
    citas = Cita.objects.all().order_by('fecha')
    return render(request, 'lista_citas.html', {'citas': citas})