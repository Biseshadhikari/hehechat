from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name = "home"),
    path('chat/<str:username>/',views.chat,name = "chat"),
    path('login/',views.login_,name = "login"),
    path('signup/',views.signup_view,name = "signup"),

    path('logout/',views.logout_view,name = "logout"),


]
