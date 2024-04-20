from django.urls import path
from .views import mostrarIndex, mostrarLogin, inicioSesion, cierreSesion, mostrarProductos, mostrarProducto, UsuarioPorCorreoApi, mostrarCarrito, agregarAlCarrito
from . import views

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('login/',mostrarLogin,name="mostrarLogin"),
    path('productos/<id_cate>',mostrarProductos,name="mostrarProductos"),
    path('producto/<id_prod>',mostrarProducto,name="mostrarProducto"),
    path('carrito',mostrarCarrito,name="mostrarCarrito"),
    path('inicioSesion/',inicioSesion, name="inicioSesion"),
    path('cierreSesion/',cierreSesion,name="cierreSesion"),
    path('agregarAlCarrito/',agregarAlCarrito,name="agregarAlCarrito"),
    path('api/categorias/', views.listaCategoriasApi.as_view(), name='api-categorias'),
    path('api/usuarios/', views.listaUsuariosApi.as_view(), name='api-usuarios'),
    path('api/productos/', views.listaProductosApi.as_view(), name='api-productos'),
    path('api/ventas/', views.listaVentasApi.as_view(), name='api-ventas'),
    path('api/detalles/', views.listaDetallesApi.as_view(), name='api-detalles'),
    path('api/compras/', views.listaComprasApi.as_view(), name='api-compras'),
    path('api/consultas/', views.listaConsultasApi.as_view(), name='api-consultas'),
    path('api/producto/', views.productoApi.as_view(), name='api-producto'),
    path('api/usuario/<str:correo>/', UsuarioPorCorreoApi.as_view(), name='usuario-por-correo'),
]