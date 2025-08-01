from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserFullSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = getattr(user, "profile", None)

        return Response({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": profile.role if profile else 1,
        })



class UserCRUDViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserFullSerializer
    permission_classes = [IsAuthenticated]


from rest_framework import  status

# accounts/views.py
from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfilePointsSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfilePointsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Profile
from .serializers import ProfileSerializer


# Obtener perfil
@api_view(['GET'])
def get_user_profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        # Retorna los datos del perfil, incluyendo el rol
        return Response({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": profile.role if profile else 1,  # Asumimos que si no tiene perfil, el rol es 1
            "avatar_url": profile.avatar_url if profile else None,  # Incluye la URL del avatar si existe
        })
    except Profile.DoesNotExist:
        return Response({"message": "Profile not found"}, status=404)


# Actualizar perfil
@api_view(['PATCH'])
def update_user_profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        
        # Actualizar los campos de usuario y perfil
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        profile.avatar_url = request.data.get('avatar_url', profile.avatar_url)
        
        # Guardar los cambios
        user.save()
        profile.save()

        # Devuelve los datos actualizados
        return Response({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": profile.role if profile else 1,
            "avatar_url": profile.avatar_url if profile else None,
        })
    except Profile.DoesNotExist:
        return Response({"message": "Profile not found"}, status=404)


# Cambiar contraseña
@api_view(['POST'])
def change_password(request):
    user = request.user
    new_password = request.data.get('password')

    if not new_password:
        return Response({"error": "Password is required."}, status=400)

    # Encriptar la nueva contraseña
    user.password = make_password(new_password)
    user.save()

    return Response({"message": "Password updated successfully."})
