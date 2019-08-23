from django.urls import path

from .views import inicio

app_name = 'base'
urlpatterns = [
    path('', inicio, name='inicio'),
]
