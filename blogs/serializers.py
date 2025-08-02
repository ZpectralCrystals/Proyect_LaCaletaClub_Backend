# blogs/serializers.py
from rest_framework import serializers
from .models import Blog
from products.models import Producto
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'titulo', 'descripcion', 'isActive', 'created_at', 'producto', 'user']
        read_only_fields = ['created_at', 'user']  # El campo 'user' será asignado automáticamente
