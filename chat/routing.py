from django.urls import re_path, path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    path(r'ws/chat/<room_name>/<str:username>/', ChatConsumer.as_asgi())
]
