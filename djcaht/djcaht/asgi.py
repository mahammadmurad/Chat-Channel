import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from . import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcaht.settings")
django_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(urls.websocket_urlpatterns),
    }
)
