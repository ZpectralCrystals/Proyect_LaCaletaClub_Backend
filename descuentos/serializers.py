# descuentos/serializers.py
from rest_framework import serializers
from .models import Descuento
from products.models import Producto
from categories.models import Categoria

class DescuentoSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Descuento
        fields = ['id', 'producto', 'descuento', 'dia', 'categoria', 'imagen', 'type', 'name', 'isActive']
