from django.shortcuts import render, redirect
## from .models import Rol, Pregunta, Categoria, Consulta, Usuario, Producto, Venta, Detalle,  Detalle_comprado
from datetime import date, timedelta
from django.utils.translation import activate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout

# Create your views here.


###No hay cuenta
def mostrarIndex(request):

    return render(request, 'core/index.html')

###Cliente

###Vendedor

###Contador

###Bodeguero

###Administrador