from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from listings.models import Band,Listing
from listings.forms import ContactUsForm
def band_list(request) :

    bands = Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})

def band_detail(request, id) :

    try:
        band = Band.objects.get(id=id)
        return render(request, 'listings/band_detail.html', {'band': band})
    except Band.DoesNotExist:
        return HttpResponse("Cette page n'existe pas")

def about(request) :
    return render(request,'listings/about.html')


def listing_list(request) :
    listings = Listing.objects.all()
    return render(request,'listings/listing_list.html',{'listings':listings})

def listing_detail(request, id) :

    try:
        listing = Listing.objects.get(id=id)
        return render(request, 'listings/listing_detail.html', {'listing': listing})
    except Band.DoesNotExist:
        return HttpResponse("Cette page n'existe pas")

def contact(request) :
    form = ContactUsForm()
    return render(request,'listings/contacts.html', {'form' : form})