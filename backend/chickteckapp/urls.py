"""chickteckproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import homefunc,signupfunc, loginfunc, logoutfunc, chat_view, usersfunc,profile_create_view
from .views import profile_update_view, profile_detail_view
from . import views

urlpatterns = [
    path('home/',homefunc,name='home'),
    path('users/', usersfunc, name='users'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path("<int:user_id>/", chat_view, name="chat"),
    path('profile/create/', profile_create_view, name='profile_create'),
    path('profile/update/', profile_update_view, name='profile_update'),
    path('profile/detail/', profile_detail_view, name='profile_detail'),
    path('communities/', views.community_list, name='community_list'),
    path('communities/create/', views.create_community, name='create_community'),
    path('communities/<int:pk>/', views.community_detail, name='community_detail'),
    path('communities/<int:pk>/join/', views.join_community, name='join_community'),
]
