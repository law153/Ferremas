from django.urls import path
from .views import mostrarIndex, mostrarLogin
from . import views

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('login/',mostrarLogin,name="mostrarLogin"),
    path('api/categorias/', views.listaCategoriasApi.as_view(), name='api-categorias'),
    
]