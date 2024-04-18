from rest_framework import serializers
from .models import Categoria, Consulta, Usuario, Producto, Venta, Detalle,  Detalle_comprado


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria','nombre_categoria']

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class consultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class detalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'

class detalleCompradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_comprado
        fields = '__all__'