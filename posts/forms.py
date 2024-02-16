from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'topic']
        widgets = {
            'topic': forms.Select(attrs={'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base bg-gray-700 focus:outline-none focus:ring-blue-500 focus:border-blue-500 border-gray-300 text-white rounded-md'}),
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base bg-gray-700 focus:outline-none focus:ring-blue-500 focus:border-blue-500 border-gray-300 text-white rounded-md'}),
        }

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'w-full px-3 py-2 rounded-md bg-white text-black focus:outline-none focus:ring focus:ring-blue-300', 'placeholder': 'Write your comment here...'}), label='')

