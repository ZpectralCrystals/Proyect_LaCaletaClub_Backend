# products/serializers.py
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'name', 'type', 'price', 'image', 'description', 'varietyOptions', 'isActive', 'isFavorite']
