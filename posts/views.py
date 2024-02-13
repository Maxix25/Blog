# In views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostForm
from authentication.models import Profile
from .models import Posts

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Form is not valid")
            form = PostForm()
            return render(request, "create_post.html", {"form": form})
        # user = User.objects.get(username = request.user)
        profile = Profile.objects.get(user = request.user)
        form.instance.author = profile
        # Save the form data to the database
        form.save()
        # Redirect to a success page or homepage
        messages.success(request, "Post created succesfully!")
        return redirect('/')  # Adjust 'home' to the name of your homepage URL
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def view_post(request, id):
    try:
        post = Posts.objects.get(id = id)
    except ObjectDoesNotExist:
        messages.error(request, "The requested post does not exist")
        return redirect("/404")
    return render(request, "view_post.html", {"post": post})