from channels.generic.websocket import AsyncWebsocketConsumer
from  channels.db import database_sync_to_async

class PersonalChatConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        my_username = self.scope['user'].username
        other_username = self.scope['url_route']['kwargs']['username']
        self.room_name = f'{my_username}-{other_username}'
        self.room_group_name = 'chat_%s'%self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.room_name
        )
        await self.accept()
    async def disconnect(self):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
