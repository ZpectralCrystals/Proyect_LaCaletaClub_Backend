from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    role = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'dni', 'first_name', 'last_name', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        dni = validated_data.pop('dni')
        role = validated_data.pop('role')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        Profile.objects.create(user=user, dni=dni, role=role)
        return user

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['dni', 'role', 'avatar_url', 'puntos']

    def validate_dni(self, value):
        user_instance = self.parent.instance  # referencia al usuario actual
        profile_instance = getattr(user_instance, 'profile', None) if user_instance else None

        if Profile.objects.exclude(id=getattr(profile_instance, 'id', None)).filter(dni=value).exists():
            raise serializers.ValidationError("Este DNI ya está registrado.")
        return value
class UserFullSerializer(serializers.ModelSerializer):
    profile = ProfileInlineSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        # Actualizar campos del usuario
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Verificar si el usuario tiene perfil
        profile = getattr(instance, 'profile', None)
        if profile:
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        else:
            # Si no existe, lo creamos
            Profile.objects.create(user=instance, **profile_data)

        return instance

class ProfileLiteSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar_url']



# accounts/serializers.py
class ProfilePointsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    dni = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'dni', 'puntos']

# serializers.py
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar_url']
