from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError



# Create your views here.

def register(request):
    if request.method == "POST":
        try:
            User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],
                email = request.POST["email"]
            )
        except IntegrityError:
            messages.error(request, "Username or email is already in use")
            return redirect("/auth/login")
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"]
        )
        if user is not None:
            messages.success(request, "Account created succesfully!")
        else:
            messages.error(request, "An error ocurred, please try again")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"]
        )
        if user is not None:
            messages.success("Login successful!")
        else:
            return redirect("/auth/login")
    
    return render(request, "login.html")