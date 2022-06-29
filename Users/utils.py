from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .forms import ProfileEditForm
from Products.models import Product


def getting_favourites(profile):
    favourites = None
    favourites_list_range = []

    for fav in profile.favourites:
        favourites_list_range.append(int(fav))
    
    if favourites_list_range:
        favourites = Product.objects.filter(id__in=favourites_list_range)

    return favourites