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

##Serializers para las tablas
class listaCategoriasApi(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer



###No hay cuenta
def mostrarIndex(request):

    categorias = obtener_categorias()

    contexto = {"categorias" : categorias}

    return render(request, 'core/index.html',contexto)

def mostrarLogin(request):

    categorias = obtener_categorias()

    contexto = {"categorias" : categorias}

    return render(request, 'core/login.html',contexto)


def obtener_categorias():
    url_servicio = 'http://localhost:8000/api/categorias/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador