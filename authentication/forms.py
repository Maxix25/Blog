from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class UsernameUpdateForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', required = True)
    class Meta:
        model = User
        fields = ['username']