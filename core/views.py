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
       
        datos = response.json()
    else:
        
        datos = {'error': 'No se pudieron obtener los datos del servicio web'}

    return render(request, 'core/index.html', {'datos': datos})

###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador