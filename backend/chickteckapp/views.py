from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import UserProfile
from .models import Chat
from .forms import ChatForm

def homefunc(request):
    return render(request,'home.html',{})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            return render(request,'signup.html', {'error': '全てのフィールドを入力してください'})
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('users')
        else:
            return render(request,'login.html',{'context':'not login'})

    return render(request,'login.html',{'context':'get method'})

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

def logoutfunc(request):
        logout(request)
        return redirect('home')

def chat_view(request, user_id=None):
    users = User.objects.exclude(id=request.user.id)
    receiver = get_object_or_404(User, id=user_id)
    
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
