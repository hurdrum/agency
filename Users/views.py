from django.shortcuts import render, redirect
from .forms import ProfileEditForm
from . import utils

def profile(request):
    page_name = 'profile'

    profile = request.user.profile
    favourites = utils.getting_favourites(profile)

    context = {
        'profile':profile,
        'page_name':page_name,
        'favorites':favourites
    }
    return render(request, 'profile.html', context)


def ProfileEdit(request):
    page_name = 'profile_edit'
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        
        return redirect('profile')

    context = {
        'page_name':page_name,
        'form':form,
        'photo':profile.photo
    }

    return render(request, 'profile-edit.html', context)