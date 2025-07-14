from django.contrib import admin

from .models import Guardian, Paciente, DetalleCita, Cita

admin.site.register(Guardian)
admin.site.register(Paciente)
admin.site.register(DetalleCita)
admin.site.register(Cita)