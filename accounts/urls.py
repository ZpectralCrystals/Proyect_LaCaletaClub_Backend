from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, MeView, UserCRUDViewSet,ProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
# ⏺ Router para registrar el CRUD de usuarios
router = DefaultRouter()
router.register(r'usuarios', UserCRUDViewSet, basename='usuarios')
router.register(r'profiles', ProfileViewSet,basename='profiles')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('', include(router.urls)),  # ⬅️ Incluye todas las rutas del ViewSet
    path('profile/', views.get_user_profile, name='get_user_profile'),
    path('profile/update/', views.update_user_profile, name='update_user_profile'),
    path('change-password/', views.change_password, name='change_password'),
]
