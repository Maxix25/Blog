from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settings, name = 'settings'),
    path('<int:user_id>', views.view_profile, name = 'view_profile')
]