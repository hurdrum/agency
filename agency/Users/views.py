from django.shortcuts import render, redirect
from .forms import ProfileEditForm

def profile(request):
    page_name = 'profile'

    user = request.user
    profile = request.user.profile
    favorites = user.favorite_prods.all()

    for fav in favorites:
        fav.pub_date = fav.pub_date.strftime("%d.%m.%Y")

    context = {
        'profile':profile,
        'page_name':page_name,
        'favorites':favorites
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