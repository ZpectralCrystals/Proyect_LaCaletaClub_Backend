from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

