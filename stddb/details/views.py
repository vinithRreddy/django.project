from django.shortcuts import render
from .models import User
from django.shortcuts import render

from .models import User
def welcome(request):
    return render(request,'welcome.html')
def admin(request):
    return render(request,'admin.py')



# Create your views here.
def login(request):
    if request.method=="POST":
        user =User
        user.name=request.POST["username"]
        user.password=request.POST["password"]
        print((user.name))
        print((user.password))
    content ={'homepage_text' :  " sign in",

              }
    return render(request, template_name='login.html',
                  context=content)