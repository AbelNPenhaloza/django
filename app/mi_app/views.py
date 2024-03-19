from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.
def saludo_view(request):
    return HttpResponse('Hola Mundo')

def crear_usuario(request):
    #Asignar directamente los valores a la instancia
    usuario = Usuario.objects.create(
        nombre ='Juan',
        apellido= 'Perez',
        edad = 30
    )
    return render(request, 'usuarios.html', {usuario:usuario})