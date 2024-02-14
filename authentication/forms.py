from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'bio': forms.Textarea(attrs = {
                'class': "focus:outline-none focus:ring-blue-500 focus:border-blue-500 text-white bg-gray-700"
            }),
            'image':forms.FileInput()
        }
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['bio'].required = False
class UsernameUpdateForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', required = True)
    class Meta:
        model = User
        fields = ['username', 'email']