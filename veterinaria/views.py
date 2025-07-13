from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Guardian

def index(request):
    return HttpResponse("Hola mundo")
# Create your views here.


def ejemplo(request):
    return JsonResponse({'mensaje': '¡Funciona!'})


def guardianes(request):
    nombre = request.GET.get('nombre', '')
    if nombre:
        guardianes = Guardian.objects.filter(nombre__icontains = nombre)
    else:
        guardianes = Guardian.objects.all()
    return render(request, 'guardianes.html', {
        "guardianes": guardianes
    })
