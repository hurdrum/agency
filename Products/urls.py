from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name = "mainpage"),
    path('card<str:pk>', views.card, name = 'card'),
]