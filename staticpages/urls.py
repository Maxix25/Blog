from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('404/', views.http_404)
]