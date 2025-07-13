from django.urls import path
from .views import ejemplo

urlpatterns = [
    path('', ejemplo),
]