# core/routing.py

from django.urls import path
from . import consumers

websocket_patterns = [
    path('ws/<str:username>/', consumers.PersonalChatConsumer.as_asgi()),
]