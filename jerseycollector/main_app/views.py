from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Jersey
from .forms import TeammateForm
# Create your views here.


class JerseyUpdate(UpdateView):
    model = Jersey
    fields = '__all__'


class JerseyDelete(DeleteView):
    model = Jersey
    success_url = '/jerseys/'


class JerseyCreate(CreateView):
    model = Jersey
    fields = '__all__'
    success_url = '/jerseys/'


def index(request):
    return render(request, 'index.html', {'title': 'Jersey Collector | Home'})


def jerseys_index(request):
    jerseys = Jersey.objects.all()
    return render(request, 'jerseys/index.html', {'title': 'All Jerseys | Jersey Collector', 'jerseys': jerseys})


def jerseys_detail(request, jersey_id):
    jersey = Jersey.objects.get(id=jersey_id)
    teammate_form = TeammateForm()
    return render(request, 'jerseys/detail.html', {'title': 'Jersey Detail | Jersey Collector', 'jersey': jersey, 'teammate_form': teammate_form})


def about(request):
    return render(request, 'about.html', {'title': 'About | Jersey Collector'})

def add_teammate(request, jersey_id):
    form = TeammateForm(request.POST)
    if form.is_valid():
        new_teammate = form.save(commit=False)
        new_teammate.jersey_id = jersey_id
        new_teammate.save()
    return redirect('detail', jersey_id=jersey_id)