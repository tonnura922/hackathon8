from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import logout

# Create your views here.
def homefunc(request):
    return render(request,'home.html',{})

def usersfunc(request):
    users = User.objects.all()
    profile = UserProfile.objects.all()
    # for i in profile:
    #     print(i.bio)
    return render(request,'users.html',{'users':users,'profile':profile})
def signupfunc(request):
        if request.method=='POST':
            username=request.POST['username']
            email = request.POST['email']
            password=request.POST['password']
            if not username or not email or not password:
                return render(request, 'signup.html', {'error': '全てのフィールドを入力してください'})
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html', {'error': 'このメールアドレスはすでに使用されています'})
            try:
                user = User.objects.create_user(username, email, password)
                return render(request,'home.html',{})
            except IntegrityError:
                return render(request,'signup.html',{'error':'このユーザーはすでに登録されています'})
        else:
            render(request,'signup.html',{})

        return render(request,'signup.html',{})

def loginfunc(request):
    pass

def logoutfunc(request):
    logout(request)
    return redirect('home')