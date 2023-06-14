from django.shortcuts import render
from django.http import HttpResponse


def hello(request) :
    return HttpResponse("Hello")

def about(request) :
    return HttpResponse("About-us")

def listings(request) :
    return HttpResponse("Listing")

def contact(request) :
    return HttpResponse("Contact us")