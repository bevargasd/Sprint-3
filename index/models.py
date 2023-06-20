from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    correo = models.EmailField(unique=True)
    # Otros campos que desees incluir

    def __str__(self):
        return self.nombre
    

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    ESPECIALIDADES = [
        ('cardiologia', 'Cardiología'),
        ('dermatologia', 'Dermatología'),
        ('ginecologia', 'Ginecología'),
        ('urología', 'Urología'),
        ('oftalmología', 'Oftalmología'),
        ('dentista', 'Dentista'),
        # Agrega otras especialidades que necesites
    ]
    especialidad = models.CharField(max_length=100, choices=ESPECIALIDADES)
    
    def __str__(self):
        return self.nombre

class Cita(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    
    def __str__(self):
        return f"{self.doctor} - {self.fecha} - {self.hora}"