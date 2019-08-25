from django.urls import path

from .views import (DepartamentoListView,
                    DepartamentoCreateView,
                    DepartamentoUpdateView,
                    DepartamentoDeleteView)

app_name = 'departamentos'
urlpatterns = [
    path('', DepartamentoListView.as_view(), name='listar'),
    path('novo/', DepartamentoCreateView.as_view(), name='novo'),
    path('atualizar/<int:pk>', DepartamentoUpdateView.as_view(), name='atualizar'),
    path('remover/<int:pk>', DepartamentoDeleteView.as_view(), name='remover'),
]
