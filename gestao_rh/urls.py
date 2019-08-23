from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.base.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
