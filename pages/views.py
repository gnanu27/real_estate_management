from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices

def index(req):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listing ,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(req, 'pages/index.html', context)

def about(req):

    realtors = Realtor.objects.order_by('hire_date')
    
    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(req, 'pages/about.html', context)