from django.urls import path
from .views import mostrarIndex
from . import views

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    path('api/categorias/', views.listaCategoriasApi.as_view(), name='api-categorias'),
    
]