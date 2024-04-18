from django.urls import path
from .views import mostrarIndex, mostrarLogin
from . import views

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('login/',mostrarLogin,name="mostrarLogin"),
    path('api/categorias/', views.listaCategoriasApi.as_view(), name='api-categorias'),
    path('api/usuarios/', views.listaUsuariosApi.as_view(), name='api-usuarios'),
    path('api/productos/', views.listaProductosApi.as_view(), name='api-productos'),
    path('api/ventas/', views.listaVentasApi.as_view(), name='api-ventas'),
    path('api/detalles/', views.listaDetallesApi.as_view(), name='api-detalles'),
    path('api/compras/', views.listaComprasApi.as_view(), name='api-compras'),
    path('api/consultas/', views.listaConsultasApi.as_view(), name='api-consultas'),
]