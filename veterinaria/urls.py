from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'guardianes', views.GuardianViewSet)
router.register(r'pacientes', views.PacienteViewSet)


urlpatterns = [
    #path('', views.ejemplo),
    #path('guardianes', views.guardianes, name='guardianes'),
    #path('pacientes', views.pacienteFormView, name='pacientes'),
    path('', include(router.urls)),
    path('guardian/cantidad/', views.guardian_count, name='guardian-count')
]