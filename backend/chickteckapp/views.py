from django.shortcuts import render
from django.contrib.auth.models import User 
from .models import UserProfile

# Create your views here.
def homefunc(request):
    return render(request,'home.html',{})

def usersfunc(request):
    users = User.objects.all()
    profile = UserProfile.objects.all()
    # for i in profile:
    #     print(i.bio)
    return render(request,'users.html',{'users':users,'profile':profile})
