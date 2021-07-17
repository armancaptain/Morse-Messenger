import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from chat import routing as chat_routing
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Morse.settings")


application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat_routing.websocket_urlpatterns,
        )
    )

})
