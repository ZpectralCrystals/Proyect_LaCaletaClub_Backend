from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

router = DefaultRouter()
router.register(r'', ProductoViewSet)  # <== Nota: sin 'productos' aquí

urlpatterns = router.urls
