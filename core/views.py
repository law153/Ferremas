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
import json
# Create your views here.

##Serializers para las tablas
class listaCategoriasApi(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializer

class listaUsuariosApi(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer

class UsuarioPorCorreoApi(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioSerializer
    lookup_field = 'correo'

class listaProductosApi(generics.ListAPIView):
    serializer_class = productoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria = self.request.query_params.get('categoria')
        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)
        return queryset
    
class productoApi(generics.ListAPIView):
    serializer_class = productoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        codigo = self.request.query_params.get('cod_prod')
        if codigo is not None:
            queryset = queryset.filter(cod_prod=codigo)
        return queryset

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

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol}

    return render(request, 'core/index.html',contexto)

def mostrarLogin(request):

    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol}

    return render(request, 'core/login.html',contexto)

def mostrarProductos(request, id_cate):

    categorias = obtener_categorias()

    productos = obtener_productos_cate(id_cate)

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "productos": productos}

    return render(request, 'core/productos.html',contexto)


def mostrarProducto(request, id_prod):

    categorias = obtener_categorias()

    producto = obtener_producto(id_prod)

    rol = request.session.get('rol',0)

    contexto = {"categorias" : categorias, "rol": rol, "producto": producto}

    return render(request, 'core/producto.html',contexto)

def obtener_categorias():
    url_servicio = 'http://localhost:8000/api/categorias/'
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None

def obtener_productos_cate(id_cate):
    url_servicio = f'http://localhost:8000/api/productos/?categoria={id_cate}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 
    
def obtener_producto(id_prod):
    url_servicio = f'http://localhost:8000/api/producto/?cod_prod={id_prod}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 
    
def obtener_usuario(correo):
    url_servicio = f'http://localhost:8000/api/usuario/{correo}'
    print(url_servicio)
    respuesta = requests.get(url_servicio)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return None 






def inicioSesion(request):
    if request.method == 'POST':
        correoI = request.POST['username']
        claveI = request.POST['password']

        try:
            user1 = User.objects.get(username=correoI)
        except User.DoesNotExist:
            return redirect('mostrarLogin')
        
        pass_valida = check_password(claveI, user1.password)
        if not pass_valida:
            return redirect('mostrarLogin')

        # Obtener usuario desde la API
        usuario_api = obtener_usuario(correoI)
        if usuario_api:
            request.session['username'] = user1.username
            request.session['rol'] = usuario_api['rol'] 
            user = authenticate(username=correoI, password=claveI)
            if user is not None:
                login(request, user)
                return redirect('mostrarIndex')
        
    return redirect('mostrarIni_sesion')
    
def cierreSesion(request):
    logout(request)
    return redirect('mostrarIndex')

###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador