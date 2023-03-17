from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django . http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        username=request.POST["txt"]
        email = request.POST["email"]
        password=request.POST["pswd"]
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.info(request,"registration succesfull")
        return redirect("index")
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["pswd"]
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("index")
    return render(request,"index.html")

