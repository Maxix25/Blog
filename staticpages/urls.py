from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('404/', views.http_404, name = '404')
]