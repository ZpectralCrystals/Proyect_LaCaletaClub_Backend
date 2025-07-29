from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/anuncios/', include('anuncios.urls')),  # <== esta línea
    path('api/categorias/', include('categorias.urls')),

]
