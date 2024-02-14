from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user_profile.forms import ProfileUpdateForm, UsernameUpdateForm

# Create your views here.

@login_required
def settings(request):
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    username_form = UsernameUpdateForm(instance = request.user)
    
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        username_form = UsernameUpdateForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and username_form.is_valid():
            profile_form.save()
            username_form.save()
            messages.success(request, "Profile updated succesfully!")
            return redirect(reverse('settings'))  # Redirect to settings page after successful update
    
    return render(request, 'settings.html', {'profile_form': profile_form, 'username_form': username_form})