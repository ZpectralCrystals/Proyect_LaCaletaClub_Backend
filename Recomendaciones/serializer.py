# recomendaciones/serializers.py
from rest_framework import serializers
from .models import Recomendaciones
from accounts.serializers import ProfileLiteSerializer

class RecomendacionSerializer(serializers.ModelSerializer):
    profile = ProfileLiteSerializer(source='userid.profile', read_only=True)

    class Meta:
        model = Recomendaciones
        fields = '__all__'
