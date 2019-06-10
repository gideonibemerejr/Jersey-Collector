from django.shortcuts import render
from .models import Jersey, jerseys
# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': 'Jersey Collector | Home'})


def jerseys_index(request):
    return render(request, 'jerseys/index.html', {'title': 'All Jerseys | Jersey Collector', 'jerseys': jerseys})


def about(request):
    return render(request, 'about.html', {'title': 'About | Jersey Collector'})
