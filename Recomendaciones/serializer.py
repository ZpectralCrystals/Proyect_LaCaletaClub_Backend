from rest_framework import serializers
from .models import Recomendaciones

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendaciones
        fields = '__all__'