from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user_profile.forms import ProfileUpdateForm, UsernameUpdateForm
from .models import Profile
from posts.models import Posts
from django.http import HttpResponse

# Create your views here.

def view_profile(request, user_id):
    user = get_object_or_404(User, id = user_id)
    profile = Profile.objects.get(user = user)
    posts = Posts.objects.filter(author = profile).count()
    recent_posts = Posts.objects.filter(author = profile).order_by('date')[:3]
    return render(request, "view_profile.html", {"profile": profile, "posts": posts, 'recent_posts': recent_posts})


@login_required
def settings(request):
    if request.method != 'POST':
            profile_form = ProfileUpdateForm(instance=request.user.profile)
            username_form = UsernameUpdateForm(instance = request.user)
            return render(request, 'settings.html', {'profile_form': profile_form, 'username_form': username_form})

    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    username_form = UsernameUpdateForm(request.POST, instance=request.user)
    
    if profile_form.is_valid() and username_form.is_valid():
        profile_form.save()
        username_form.save()
        messages.success(request, "Profile updated succesfully!")
        return redirect(reverse('settings'))  # Redirect to settings page after successful update
    else:
        return HttpResponse(profile_form.errors)