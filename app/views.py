from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)

        myuser = User.object.create(username=username, email=email, password=password)
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, 'signUp.html')

def sigin(request):
    return render(request, 'signIn.html')

def activate(request, uidb64, token):
    pass

def signout(request):
    pass