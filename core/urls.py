from django.urls import path
from .views import mostrarIndex

urlpatterns=[

    ###No cuenta
    path('',mostrarIndex,name="mostrarIndex"),
    
]