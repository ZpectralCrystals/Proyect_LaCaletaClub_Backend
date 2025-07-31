from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecomendacionViewSet

router = DefaultRouter()
router.register(r'recomendaciones', RecomendacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]