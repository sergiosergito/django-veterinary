from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Guardian, Paciente
from .forms import PacienteForm

from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import GuardianSerializer, PacienteSerializer


def index(request):
    return HttpResponse("Hola mundo")
# Create your views here.


def ejemplo(request):
    return JsonResponse({'mensaje': '¡Funciona!'})


def guardianes(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Guardian(nombre = post_nombre)
        q.save()

    nombre = request.GET.get('nombre', '')
    if nombre:
        guardianes = Guardian.objects.filter(nombre__icontains = nombre)
    else:
        guardianes = Guardian.objects.all()
    return render(request, 'form_guardianes.html', {
        "guardianes": guardianes
    })

def pacienteFormView(request):
    form = PacienteForm()
    paciente = None

    id_paciente = request.GET.get('id')
    if id_paciente:
        paciente = get_object_or_404(Paciente, id=id_paciente)
        form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        if paciente:
            form = PacienteForm(request.POST, instance=paciente)
        else:
            form = PacienteForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'form_pacientes.html', {
        "form": form
    })

class GuardianViewSet(viewsets.ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

@api_view(['GET'])
def guardian_count(request):
    try:
        cantidad = Guardian.objects.count()
        return JsonResponse({
                'cantidad': cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
