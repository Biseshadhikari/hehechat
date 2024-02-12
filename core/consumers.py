from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from .models import *

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_username = self.scope['user'].username
        other_username = self.scope['url_route']['kwargs']['username']

        # Sort the usernames alphabetically
        usernames = sorted([my_username, other_username])

        # Join the sorted usernames with a hyphen
        self.room_name = '-'.join(usernames)
        self.room_group_name = f'chat_{self.room_name}'

            
        # print(self.room_group_name)  # Fix the room_group_name format
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name  # Fix the group_add channel_name argument
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        chatType = data['type']
        
        if chatType == "message":
            await self.save_message(username,self.room_group_name,message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.message',  # Fix the type name
                    'message': message,
                    'username': username
                }
            )
        else:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.typing',  # Fix the type name
                    'message': message,
                    'username': username
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'type':"message",
            'message': message,
            'username': username
        }))
    async def chat_typing(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'type':"typing",
            'message': message,
            'username': username
        }))
    @database_sync_to_async
    def save_message(self,username,thread_name,message):
        chat = Chats.objects.create(sender = username, group = thread_name,content = message)
        # chat.save()