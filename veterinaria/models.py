from django.db import models

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
    peso = models.DecimalField(max_digits=2, decimal_places=2)
    alto = models.DecimalField(max_digits=2, decimal_places=2)
    largo = models.DecimalField(max_digits=2, decimal_places=2)
    entero = models.BooleanField(blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


