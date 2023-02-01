from math import prod
from django.shortcuts import render
from .models import Product, Job
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Users.models import Profile



def card(request, pk):
    page_name = 'card'

    card = Product.objects.get(id=pk)
    
    context = {
        'card':card,
        'page_name':page_name,
    }
        
    return render(request, 'card.html', context)


def mainpage(request):
    page_name = 'mainpage'
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    cards = Product.objects.filter(title__icontains=search, isVIP=False)

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

    VIPproducts = Product.objects.filter(isVIP=True)

    jobs = Job.objects.all()

    context = { 
        'cards':cards,
        'VIPproducts': VIPproducts,
        'page_name':page_name,
        'paginator':paginator,
        'jobs': jobs
    }

    return render(request, 'mainpage.html', context)