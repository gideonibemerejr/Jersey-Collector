from django.shortcuts import render
from .models import Jersey
# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': 'Jersey Collector | Home'})


def jerseys_index(request):
    jerseys = Jersey.objects.all()
    return render(request, 'jerseys/index.html', {'title': 'All Jerseys | Jersey Collector', 'jerseys': jerseys})


def jerseys_detail(request, jersey_id):
    jersey = Jersey.objects.get(id=jersey_id)
    return render(request, 'jerseys/detail.html', {'title': 'Jersey Detail | Jersey Collector', 'jersey': jersey})


def about(request):
    return render(request, 'about.html', {'title': 'About | Jersey Collector'})
