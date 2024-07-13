from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

def homefunc(request):
    return render(request,'home.html',{})

def loginfunc(request):
    if request.method == 'post':
        username = request.POST['userame']
        email = request.POST['email']
        password = request.POST['password']
        if not username or not email or not password:
            return render(request,'signup.html', {'error': '全てのフィールドを入力してください'})
        user = authenticate(request,username=username,password=password,email=email)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'context':'not login'})

    return render(request,'login.html',{'context':'get method'})