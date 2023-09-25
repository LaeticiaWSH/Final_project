from django.shortcuts import render
from itertools import groupby
from django.http import HttpResponse # pass view information into the browser
from .models import Donut

# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're in the donut website.")
# Create your views here.


def home (request):
    return render(request,'home.html',{})

# def menu(request):
#     donuts = Donut.objects.all()
#     return render(request, 'menu.html', {'donuts': donuts})
def menu(request):
    donuts = Donut.objects.all().order_by('category', 'name')  # Retrieve all donuts and order them by category and name
    donuts_by_category = {}
    
    for category, items in groupby(donuts, key=lambda x: x.category):
        donuts_by_category[category] = list(items)

    return render(request, 'menu.html', {'donuts_by_category': donuts_by_category})
