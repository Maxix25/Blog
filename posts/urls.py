from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name = "create_post"),
    path('view/<int:post_id>/', views.view_post, name = "view_post"),
    path('post_comment/<int:post_id>/', views.post_comment, name='post_comment'),
]