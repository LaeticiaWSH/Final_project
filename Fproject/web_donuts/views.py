from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response
def index(request):
    return HttpResponse("Hello, world. You're in the donut website.")
# Create your views here.

# from .models import Donut


# def landing (request):
#     return render(request,'landing.html',{})
# def menu(request):
#     donuts = Donut.objects.all()
#     return render(request, 'menu.html', {'donuts': donuts})