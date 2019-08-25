from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('', include('apps.base.urls')),
                  path('funcionario/', include('apps.funcionarios.urls')),
                  path('departamento/', include('apps.departamentos.urls')),
                  path('empresa/', include('apps.empresas.urls')),
                  path('documento/', include('apps.documentos.urls')),
                  path('conta/', include('django.contrib.auth.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
