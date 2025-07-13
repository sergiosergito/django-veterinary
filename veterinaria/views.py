from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hola mundo")
# Create your views here.


def ejemplo(request):
    return JsonResponse({'mensaje': '¡Funciona!'})