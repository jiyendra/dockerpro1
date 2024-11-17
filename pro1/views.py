
from django.http import HttpResponse
from django.shortcuts import render


def page(request):
    dic1 = {'name': 'manago', 'place': 'Delhi', 'person': 'Rajesh'}
    return render(request, 'index.html', dic1)


def index(request):
    return HttpResponse("<h1>hello world</h1>")


def product(request):
    return HttpResponse("products are not available")
