from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
    
def services(request):
    return render(request, "services.html")

def properties(request):
    return render(request, "properties.html")

def property_details(request):
    return render(request, "property-single.html")

