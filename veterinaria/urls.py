from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'guardianes', views.GuardianViewSet)

urlpatterns = [
    #path('', views.ejemplo),
    #path('guardianes', views.guardianes, name='guardianes'),
    #path('pacientes', views.pacienteFormView, name='pacientes'),
    path('', include(router.urls)),
]