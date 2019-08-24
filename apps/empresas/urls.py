from django.urls import path

from .views import EmpresaCreateView, EmpresaUpdateView

app_name = 'empresas'
urlpatterns = [
    path('nova/', EmpresaCreateView.as_view(), name='criar'),
    path('editar/<int:pk>', EmpresaUpdateView.as_view(), name='editar'),
]
