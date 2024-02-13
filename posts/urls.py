from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name = "Create Post"),
    path('view/<int:id>/', views.view_post, name = "View Post")
]