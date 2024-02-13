from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "index.html")


def http_404(request):
    return render(request, "404.html")