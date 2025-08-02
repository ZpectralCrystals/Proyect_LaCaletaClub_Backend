# recomendaciones/serializers.py
from rest_framework import serializers
from .models import Recomendaciones
from django.contrib.auth.models import User

class RecomendacionesSerializer(serializers.ModelSerializer):
    userid = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Recomendaciones
        fields = ['id', 'description', 'isActive', 'created_at', 'userid']
def create(self, validated_data):
        return Recomendaciones.objects.create(**validated_data)