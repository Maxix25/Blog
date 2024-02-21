from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.

def register(request):
    if request.method == "POST":
        if request.POST["password"] != request.POST["confirm_password"]:    # Check if passwords match
            messages.error("Passwords do not match")
            return redirect(reverse('register'))
        try:
            # Create user in database
            User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],
                email = request.POST["email"]
            )
        except IntegrityError:
            # Username is already in use
            messages.error(request, "Username or email is already in use")
            return redirect(reverse('register'))
        # Authenticate user
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"]
        )
        if user is None:
            messages.error(request, "An error ocurred, please try again")
            return redirect(reverse('register'))
        messages.success(request, "Account created succesfully, you may now login")
        return redirect(reverse('login'))
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"]
        )
        if user is None:
            messages.error(request, "Credentials are not valid")
            return redirect(reverse('login'))
        messages.success(request, "Logged in succesfully!")
        auth_login(request, user)
        if request.GET.get('next'): # If the user tried to access a login required view, redirect to that page after login
            return redirect(request.GET["next"])
        return redirect("/")
    return render(request, "login.html")



@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out succesfully!")
    return redirect(reverse('login'))