from django.shortcuts import render
from django.db.models import Count
from posts.models import Posts


# Create your views here.

def homepage(request):
    recent_posts = Posts.objects.all().order_by('-date')
    featured_posts = Posts.objects.annotate(num_comments=Count('post')).order_by('-num_comments')
    return render(request, "index.html", {"recent_posts": recent_posts, "featured_posts": featured_posts})


def http_404(request):
    return render(request, "404.html")