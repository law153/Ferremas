from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.contrib import messages
from core.serializers import categoriaSerializer, usuarioSerializer, productoSerializer, consultaSerializer, ventaSerializer, detalleSerializer, detalleCompradoSerializer
from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle,  Detalle_comprado
import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
# Create your views here.

##Serializers para las tablas
class listaCategoriasApi(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer

class listaUsuariosApi(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer

class listaProductosApi(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = productoSerializer

class listaVentasApi(generics.ListAPIView):
    queryset = Venta.objects.all()
    serializer_class = ventaSerializer

class listaConsultasApi(generics.ListAPIView):
    queryset = Consulta.objects.all()
    serializer_class = consultaSerializer

class listaDetallesApi(generics.ListAPIView):
    queryset = Detalle.objects.all()
    serializer_class = detalleSerializer

class listaComprasApi(generics.ListAPIView):
    queryset = Detalle_comprado.objects.all()
    serializer_class = detalleCompradoSerializer




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


def inicioSesion(request):
    
    correoI = request.POST['correo_ini']
    claveI = request.POST['contra_ini']

    try:
        user1 = User.objects.get(username = correoI)
    except User.DoesNotExist:
        
        return redirect('mostrarLogin')
    
    pass_valida = check_password(claveI, user1.password)
    if not pass_valida:
        
        return redirect('mostrarLogin')
    usuario = Usuario.objects.get(correo = correoI, clave = claveI)
    user = authenticate(username = correoI, password = claveI)
    if user is not None:
        login(request, user)
        request.session['username'] = user1.username
        return redirect('mostrarIndex')

    else:
       
        return redirect('mostrarIni_sesion')
    
###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador