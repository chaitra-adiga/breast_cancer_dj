from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html',{})

def login_user(request):  # we can't call it login because it wiil conflict with built-in function
    pass

def logout_user(request):
    pass

