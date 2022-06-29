from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.profile, name = 'profile'),
    path('profile-edit/', views.ProfileEdit, name = 'profile-edit')
]