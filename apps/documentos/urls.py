from django.urls import path

from .views import (DocumentoCreateView, )

app_name = 'documentos'
urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentoCreateView.as_view(), name='novo'),
]
