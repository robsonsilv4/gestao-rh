from django.urls import path

from .views import (HoraExtraListView,
                    HoraExtraCreateView,
                    HoraExtraUpdateView,
                    HoraExtraDeleteView)

app_name = 'horas_extras'
urlpatterns = [
    path('', HoraExtraListView.as_view(), name='listar'),
    path('adicionar/', HoraExtraCreateView.as_view(), name='adicionar'),
    path('atualizar/<int:pk>', HoraExtraUpdateView.as_view(), name='atualizar'),
    path('remover/<int:pk>', HoraExtraDeleteView.as_view(), name='remover'),
]
