from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto  # Importa el modelo Producto

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        # Crea una nueva instancia de Producto con los datos proporcionados
        nuevo_producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
        nuevo_producto.save()  # Guarda el nuevo producto en la base de datos

        return HttpResponse('Producto creado exitosamente!')
    else:
        return render(request, 'crear_producto.html')