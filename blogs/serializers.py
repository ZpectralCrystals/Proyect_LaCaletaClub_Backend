from rest_framework import serializers
from .models import Blog
from accounts.serializers import ProfileLiteSerializer

class BlogSerializer(serializers.ModelSerializer):
    profile = ProfileLiteSerializer(source='userid.profile', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
