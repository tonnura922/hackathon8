from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Chat
from .forms import ChatForm

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

@login_required
def chat_view(request, user_id=None):
    
        # ログインユーザー以外のユーザー一覧を取得する
    users = User.objects.exclude(id=request.user.id)
    receiver = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.receiver = receiver
            chat.save()
            return redirect('chat', user_id=user_id)
    else:
        form = ChatForm()

    messages = Chat.objects.filter(sender=request.user, receiver=receiver) | Chat.objects.filter(sender=receiver, receiver=request.user)
    messages = messages.order_by('created_at')




    return render(request, 'chatpage.html', {'form': form, 'users': users, 'receiver': receiver, 'messages': messages})
