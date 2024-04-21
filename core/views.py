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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class FiltrarCarritoAPI(APIView):
    def get(self, request):
        # Obtener los parámetros de consulta de la URL
        usuario = request.GET.get('usuario')
        estado = request.GET.get('estado')

        # Filtrar usuarios basados en los parámetros
        carrito = Venta.objects.all()
        if carrito:
            carrito = carrito.filter(usuario=usuario)
        if estado:
            carrito = carrito.filter(estado=estado)

        # Serializar los resultados y devolver la respuesta
        serializer = ventaSerializer(carrito, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



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

def mostrarCarrito(request):
    categorias = obtener_categorias()

    rol = request.session.get('rol',0)

    username = request.session.get('username')
    usuario1 = Usuario.objects.get(correo = username)

    carrito = Venta.objects.filter(usuario = usuario1, estado='ACTIVO').first()

    if carrito:
        detalles = Detalle.objects.filter(venta = carrito)
        totalV = 0
        for i in detalles:

            if i.producto.stock <= 0:
                i.delete()
                messages.warning(request,'Un producto de su carrito se quedó sin stock')
                return redirect('mostrarCarritoCli')
                    
            totalV += i.subtotal
        carrito.total = totalV
        carrito.save()
        contexto = {"categorias" : categorias, "carrito" : detalles, "venta" : carrito}
        if not detalles:
            carrito.estado = 'INACTIVO'
            carrito.save()
    else:
        contexto = {"categorias" : categorias, "rol": rol}
        messages.warning(request,'No hay productos en el carrito actualmente')

    
    return render(request, 'core/carrito.html',contexto)

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


def agregarAlCarrito(request):
    cod_produc = request.POST['codigo']
    productoC = Producto.objects.get(cod_prod = cod_produc)

    username = request.session.get('username')
    usuarioC = Usuario.objects.get(correo = username)
        
    fecha_hoy = date.today()
    entrega = timedelta(999)
    fecha_e = fecha_hoy + entrega

    carrito = Venta.objects.filter(usuario = usuarioC, estado='ACTIVO').first()

    if carrito:
        detalle1 = Detalle.objects.filter(venta = carrito, producto = productoC)
        if detalle1:
            detalle = Detalle.objects.get(venta = carrito, producto = productoC)
            detalle.cantidad += 1
            detalle.subtotal += productoC.precio
            detalle.save()

                
        else:
            Detalle.objects.create(cantidad = 1,subtotal = productoC.precio,venta = carrito,producto = productoC)


    else:
        carrito = Venta.objects.create(fecha_venta = fecha_hoy,estado = "ACTIVO",fecha_entrega = fecha_e,total = productoC.precio, carrito = 1, usuario = usuarioC)

        Detalle.objects.create(cantidad = 1,subtotal = productoC.precio,venta = carrito, producto = productoC)
            
    return redirect('mostrarCarrito')

def sacarDelCarro(request, cod_detalle):
    
    detalle = Detalle.objects.get(id_detalle = cod_detalle)
    detalle.delete()
        

    return redirect('mostrarCarrito')
   

def cambiarCantidad(request, cod_detalle):

    detalle = Detalle.objects.get(id_detalle = cod_detalle)
    cant = int(request.POST['nueva_cantidad_{}'.format(cod_detalle)])
    producto = Producto.objects.get(cod_prod = detalle.producto.cod_prod)

    stockC = producto.stock
    cantidadC = int(cant)

    if cantidadC >= 0:
        if cantidadC <= stockC:
            detalle.cantidad = cantidadC
            detalle.subtotal = detalle.producto.precio * cantidadC
            detalle.save()
            return redirect('mostrarCarrito')
        else:
            messages.warning(request,'La cantidad no puede exceder el stock disponible')
            return redirect('mostrarCarrito')
    else:
        messages.warning(request,'La cantidad no puede ser menor a 1')
        return redirect('mostrarCarrito')
