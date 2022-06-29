from math import prod
from django.shortcuts import render
from .models import Product, Price
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Users.models import Profile



def card(request, pk):
    page_name = 'card'

    card = Product.objects.get(id=pk)

    # profile = request.user.profile

    # if pk in profile.favourites:
    #     value = 'Удалить из избранного'
    # else:
    #     value = 'Добавить в избранное'

    # if request.method == "POST":

    #     if pk in profile.favourites:
    #         new_profile_favourites = profile.favourites.replace(pk, '')
    #         profile.favourites = new_profile_favourites
    #     else:
    #         profile.favourites += pk

    #     profile.save()
    
    context = {
        'card':card,
        'page_name':page_name,
        # 'value':value
    }
        
    return render(request, 'card.html', context)


def mainpage(request):
    page_name = 'mainpage'
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    cards = Product.objects.filter(title__icontains=search)

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(cards, results)

    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        cards = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        cards = paginator.page(page)

    prices_sale = Price.objects.filter(status = 'Продажа')
    prices_rent = Price.objects.filter(status = 'Аренда')

    context = { 
        'cards':cards,
        'prices_sale':prices_sale,
        'prices_rent':prices_rent,
        'page_name':page_name,
        'paginator':paginator
    }

    return render(request, 'mainpage.html', context)