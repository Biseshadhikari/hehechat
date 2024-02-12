from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def index(request):
    if request.user.is_authenticated:
        users = User.objects.exclude(id = request.user.id)
        return render(request,'core/index.html',{'users':users})
    else:
         return redirect('login')


def chat(request,username):
    if request.user.is_authenticated:
        users = User.objects.exclude(id=request.user.id)
        chat_user = User.objects.filter(username=username).first()

        # Sort the usernames alphabetically
        usernames = sorted([request.user.username, username])

        # Join the sorted usernames with a hyphen
        group = f'chat_{"-".join(usernames)}'  
        message_obj = Chats.objects.filter(group = group)
        print(message_obj)
        return render(request,'core/main_chat.html',{'users':users,'chat_user':chat_user,'username':username,'message_obj':message_obj})
    else:
         return redirect('login')

def login_(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your home page or any other page
            else:
                    return render(request, 'core/login.html', {'error': 'Invalid credentials'})

        return render(request,'core/login.html')
    else:
         return redirect('/')
    

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Basic validation
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'signup.html')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        # You can add more sophisticated validation here as needed

        # Create the user if validation passes
        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('home')  # Redirect to your home page or any other page

    return render(request, 'core/signup.html')   
    
def logout_view(request):
    logout(request)
    return redirect('login')