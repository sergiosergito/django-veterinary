from django.db import models

from .validators import esMayorACero, esMenorACien


class Guardian(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class PatientUnits(models.TextChoices):
    CM = 'cm', 'Centimetros'
    KG = 'kg', 'Kilogramos'

class Paciente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    raza = models.TextField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, validators=[esMayorACero, esMenorACien])
    alto = models.DecimalField(max_digits=5, decimal_places=2, validators=[esMayorACero, ])
    largo = models.DecimalField(max_digits=5, decimal_places=2, validators=[esMayorACero])
    entero = models.BooleanField(blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cita(models.Model):
    veterinario = models.CharField(max_length=100, unique=True)
    realizada = models.BooleanField(blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DetalleCita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    tratamiento = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
