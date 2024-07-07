from django.shortcuts import render

# Create your views here.
def homefunc(request):
    return render(request,'home.html',{})