from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.utils.translation import activate
from django.contrib import messages
from core.serializers import categoriaSerializer
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle,  Detalle_comprado
import requests
# Create your views here.


class listaCategoriasApi(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer

###No hay cuenta
def mostrarIndex(request):

    return render(request, 'core/index.html')


def obtener_categorias(request):
    # URL del servicio web desde el cual deseas obtener los datos
    url_servicio_web = 'http://localhost:8000/api/categorias/'

    # Realiza una solicitud GET al servicio web
    response = requests.get(url_servicio_web)

    if response.status_code == 200:
        # Obtén los datos en formato JSON
        datos = response.json()
        print('Datos obtenidos:', datos)
        # Instancia el serializer con los datos recibidos
        serializer = categoriaSerializer(data=datos['categorias'], many=True)

        # Verifica si los datos son válidos según el serializer
        if serializer.is_valid():
            # Obtiene los datos serializados
            categorias_serializadas = serializer.data
        else:
            # Si los datos no son válidos, muestra un error
            categorias_serializadas = {'error': 'Error al procesar los datos del servicio web'}
    else:
        categorias_serializadas = {'error': 'No se pudieron obtener los datos del servicio web'}

    # Pasa los datos serializados a la plantilla
    return render(request, 'core/index.html', {'categorias_serializadas': categorias_serializadas})

###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador