from django.urls import path , include
from VChat_App.consumers import ChatConsumer

websocket_urlpatterns = [
    path("" , ChatConsumer.as_asgi()) , 
] 