from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.base.urls')),
    path('funcionario/', include('apps.funcionarios.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('conta/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
