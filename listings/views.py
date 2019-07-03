from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices
# Create your views here.

def index(req):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = req.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        'listing': paged_listings
    }
    paginator = (listings, 3)
    return render(req, 'listings/listings.html', context)

def listing(req, listing_id): 
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(req, 'listings/listing.html', context)

def search(req):
    queryset_list = Listing.objects.order_by('-list_date')

    #keyword

    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        
        if keywords: 
            queryset_list = queryset_list.filter(description__icontains = keywords) 
        
    if 'city' in req.GET: 
            city = req.GET['city']
            if city:
                queryset_list = queryset_list.filter(city__iexact = city)
        
    if 'state' in req.GET: 
        state = req.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

    if 'bedrooms' in req.GET: 
        bedrooms = req.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    if 'price' in req.GET: 
        price = req.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)


        

    context={
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': req.GET  
    }
    return render(req, 'listings/search.html', context)