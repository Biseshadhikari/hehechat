from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chats(models.Model): 
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    sender = models.CharField(max_length = 200)
    group = models.CharField(max_length = 200)

