import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application

from chat.routing import websocket_urlpatterns

import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socketproject.settings")
django_asgi_app = get_asgi_application()
django_wsgi_app = get_wsgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    ),
})
