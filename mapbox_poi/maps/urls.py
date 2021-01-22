from django.urls import path

from .views import map_view

app_name = 'maps'

urlpatterns = [
    path('', map_view, name='map_view'),
]
