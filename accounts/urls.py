from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, MeView, UserCRUDViewSet,ProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views



# ⏺ Router para registrar el CRUD de usuarios
router = DefaultRouter()
router.register(r'usuarios', UserCRUDViewSet, basename='usuarios')
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = [
    # Rutas de autenticación
    path('register/', RegisterView.as_view(), name='register'),  # Registro de usuario
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener JWT
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Actualizar JWT
    path('me/', MeView.as_view(), name='me'),  # Obtener el perfil del usuario autenticado

    # Rutas CRUD para usuarios y perfiles
    path('', include(router.urls)),  # Incluye todas las rutas de los ViewSets

    # Rutas de perfil
    path('profile/', views.get_user_profile, name='get_user_profile'),  # Obtener perfil de usuario
    path('profile/update/', views.update_user_profile, name='update_user_profile'),  # Actualizar perfil de usuario

    # Rutas de cambio de contraseña
    path('change-password/', views.change_password, name='change_password'),
    path('user/puntos/', views.get_user_points, name='get_user_points'),
]
