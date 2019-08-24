from django.urls import path

from .views import (FuncionarioListView,
                    FuncionarioCreateView,
                    FuncionarioUpdateView,
                    FuncionarioDeleteView)

app_name = 'funcionarios'
urlpatterns = [
    path('', FuncionarioListView.as_view(), name='listar'),
    path('novo/', FuncionarioCreateView.as_view(), name='novo'),
    path('editar/<int:pk>', FuncionarioUpdateView.as_view(), name='editar'),
    path('remover/<int:pk>', FuncionarioDeleteView.as_view(), name='remover'),
]
