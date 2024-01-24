from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Chats(models.Model): 
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    sender = models.ForeignKey(User, on_delte = models.CASCADE)
    receiver = models.ForeignKey(User, on_delte = models.CASCADE)