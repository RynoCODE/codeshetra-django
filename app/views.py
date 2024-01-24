from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'signup.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'signin.html')

def signout(request):
    pass