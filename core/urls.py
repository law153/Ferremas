from django.urls import path
from .views import mostrarIndex, mostrarLogin, inicioSesion, cierreSesion, mostrarProductos, mostrarProducto, UsuarioPorCorreoApi, mostrarCarrito, agregarAlCarrito, cambiarCantidad, sacarDelCarro, DetallePorIdApi, VentaPorIdApi
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
    path('cambiarCantidad/<cod_detalle>',cambiarCantidad,name="cambiarCantidad"),
    path('sacarDelCarro/<cod_detalle>',sacarDelCarro,name="sacarDelCarro"),
    path('agregarAlCarrito/',agregarAlCarrito,name="agregarAlCarrito"),
    path('api/categorias/', views.listaCategoriasApi.as_view(), name='api-categorias'),
    path('api/usuarios/', views.listaUsuariosApi.as_view(), name='api-usuarios'),
    path('api/productos/', views.listaProductosApi.as_view(), name='api-productos'),
    path('api/ventas/', views.listaVentasApi.as_view(), name='api-ventas'),
    path('api/detalles/', views.listaDetallesApi.as_view(), name='api-detalles'),
    path('api/compras/', views.listaComprasApi.as_view(), name='api-compras'),
    path('api/consultas/', views.listaConsultasApi.as_view(), name='api-consultas'),
    path('api/producto/', views.productoApi.as_view(), name='api-producto'),
    path('api/detallesProducto/', views.listaDetallesProductoApi.as_view(), name='api-detalles-producto'),
    path('api/usuario/<str:correo>/', UsuarioPorCorreoApi.as_view(), name='usuario-por-correo'),
    path('api/filtrar-carrito/', views.FiltrarCarritoAPI.as_view(), name='filtrar-carrito'),
    path('api/detalles-carrito/', views.DetallesCarritoAPI.as_view(), name='detalles-carrito'),
    path('api/detalles-buscar-carrito/', views.DetallesBuscarCarritoAPI.as_view(), name='detalles-buscar-carrito'),
    path('api/detalle/<str:id_detalle>/', DetallePorIdApi.as_view(), name='detalle-por-id'),
    path('api/venta/<str:id_detalle>/', VentaPorIdApi.as_view(), name='venta-por-id'),
]