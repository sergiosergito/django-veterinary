from django.urls import path
from . import views

urlpatterns = [
    path('', views.ejemplo),
    path('guardianes', views.guardianes, name='guardianes'),
    path('pacientes', views.pacienteFormView, name='pacientes'),

]