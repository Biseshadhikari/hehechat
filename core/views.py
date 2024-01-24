from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    users = User.objects.exclude(id = request.user.id)
    return render(request,'core/index.html',{'users':users})


def chat(request,pk):
    users = User.objects.exclude(id = request.user.id)
    chat_user = User.objects.filter(pk = pk).first()
    return render(request,'core/main_chat.html',{'users':users,'chat_user':chat_user,'pk':pk})