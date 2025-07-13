from django.contrib import admin

from .models import Guardian, Paciente

admin.site.register(Guardian)
admin.site.register(Paciente)