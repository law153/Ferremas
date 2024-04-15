from rest_framework import serializers
from core.models import Categoria


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria','nombre_categoria']