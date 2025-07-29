from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnuncioViewSet

router = DefaultRouter()
router.register(r'', AnuncioViewSet)  # Opcional: puedes usar 'anuncios' también

urlpatterns = [
    path('', include(router.urls)),
]
