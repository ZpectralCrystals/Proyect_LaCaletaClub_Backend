# anuncios/serializers.py
from rest_framework import serializers
from .models import Anuncio

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['id', 'titulo', 'mensaje', 'imagen', 'activo']
