from django.contrib import admin
from .models import Detalle, Rol, Pregunta, Categoria, Usuario, Producto, Venta, Consulta, Detalle_comprado
# Register your models here.


admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle)
admin.site.register(Consulta)
admin.site.register(Detalle_comprado)
