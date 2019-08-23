from django.urls import path

from .views import inicio

app_name = 'funcionarios'
urlpatterns = [
    path('', inicio, name='inicio'),
]
