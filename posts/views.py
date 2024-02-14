# In views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .forms import PostForm, CommentForm
from user_profile.models import Profile
from .models import Posts, Comment

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

@login_required
def view_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    comments = Comment.objects.filter(post = post)
    comment_form = CommentForm()
    return render(request, 'view_post.html', {'post': post, 'comments': comments, "comment_form": comment_form})

@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Comment.objects.create(post=post, name=request.user.profile, content=content)
            messages.success(request, "Comment posted succesfully!")
            return redirect('view_post', post_id = post_id)
    return redirect('view_post', post_id=post_id)