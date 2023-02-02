from .models import Product, Job
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
import json
from django.utils.dateparse import parse_datetime
import datetime


def card(request, pk):
    page_name = 'card'
    user = request.user

    card = Product.objects.get(id=pk)
    card.isFavotite = False
    if request.user.is_authenticated and user.favorite_prods.filter(id=pk):
        card.isFavorite = True

    card.pub_date = card.pub_date.strftime("%d.%m.%Y")

    context = {
        'card':card,
        'page_name':page_name,
    }
        
    return render(request, 'card.html', context)


def mainpage(request):
    page_name = 'mainpage'
    search = ''
    user = request.user

    if request.GET.get('search'):
        search = request.GET.get('search')

    VIPproducts = Product.objects.filter(isVIP=True)
    jobs = Job.objects.all()
    cards = Product.objects.filter(title__icontains=search, isVIP=False)

    for card in cards:
        card.pub_date = card.pub_date.strftime("%d.%m.%Y")
    for card in VIPproducts:
        card.pub_date = card.pub_date.strftime("%d.%m.%Y")

    if request.user.is_authenticated:
        for card in VIPproducts:
            card.isFavourite = False
            if user.favorite_prods.filter(id = card.id):
                card.isFavourite = True

        for card in cards:
            card.isFavourite = False
            if user.favorite_prods.filter(id = card.id):
                card.isFavourite = True


    page = request.GET.get('page')
    results = 6
    paginator = Paginator(cards, results)

    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        cards = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        cards = paginator.page(page)

    context = { 
        'cards':cards,
        'VIPproducts': VIPproducts,
        'page_name':page_name,
        'paginator':paginator,
        'jobs': jobs
    }

    return render(request, 'mainpage.html', context)

def like(request):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            id = json.loads(request.body.decode('utf-8'))['id']
            if user.favorite_prods.filter(id = id):
                user.favorite_prods.remove(Product.objects.get(id = id))
            else:
                user.favorite_prods.add(Product.objects.get(id = id))
            return HttpResponse()
        else:
            return HttpResponse(status=403)
