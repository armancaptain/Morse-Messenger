from django.urls import path
from .views import index, room

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/<str:username>/', room, name='room'),
]