from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import TeammateForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
from .models import Jersey, Teammate, Photo
# Create your views here.

BUCKET = 'jerseycollecter'
S3_BASE_URL = f'https://{BUCKET}.s3.amazonaws.com/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class JerseyUpdate(LoginRequiredMixin, UpdateView):
    model = Jersey
    fields = '__all__'


class JerseyDelete(LoginRequiredMixin, DeleteView):
    model = Jersey
    success_url = '/jerseys/'


class JerseyCreate(LoginRequiredMixin, CreateView):
    model = Jersey
    fields = '__all__'
    success_url = '/jerseys/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def home(request):
    return render(request, 'index.html', {'title': 'Jersey Collector | Home'})


@login_required
def jerseys_index(request):
    jerseys = Jersey.objects.filter(user=request.user)
    return render(request, 'jerseys/index.html', {'title': 'All Jerseys | Jersey Collector', 'jerseys': jerseys})


@login_required
def jerseys_detail(request, jersey_id):
    jersey = Jersey.objects.get(id=jersey_id)
    teammates_jersey_doesnt_have = Teammate.objects.exclude(id__in=jersey.teammates.all().values_list('id'))
    return render(request, 'jerseys/detail.html', {'title': 'Jersey Detail | Jersey Collector', 'jersey': jersey, 'teammates': teammates_jersey_doesnt_have})


def about(request):
    return render(request, 'about.html', {'title': 'About | Jersey Collector'})


@login_required
def add_teammate(request, jersey_id):
    form = TeammateForm(request.POST)
    if form.is_valid():
        new_teammate = form.save(commit=False)
        new_teammate.jersey_id = jersey_id
        new_teammate.save()
    return redirect('detail', jersey_id=jersey_id)


@login_required
def assoc_teammate(request, jersey_id, teammate_id):
    Jersey.objects.get(id=jersey_id).teammates.add(teammate_id)
    return redirect('detail', jersey_id=jersey_id)


@login_required
def unassoc_teammate(request, jersey_id, teammate_id):
    Jersey.objects.get(id=jersey_id).teammates.remove(teammate_id)
    return redirect('detail', jersey_id=jersey_id)


class TeammateList(LoginRequiredMixin, ListView):
    model = Teammate


class TeammateDetail(LoginRequiredMixin, DetailView):
    model = Teammate


class TeammateCreate(LoginRequiredMixin, CreateView):
    model = Teammate
    fields = '__all__'


class TeammateUpdate(LoginRequiredMixin, UpdateView):
    model = Teammate
    fields = '__all__'


class TeammateDelete(LoginRequiredMixin, DeleteView):
    model = Teammate
    success_url = '/teammates/'


@login_required
def add_photo(request, jersey_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{key}"
            # we can assign to jersey_id or jersey (if you have a jersey object)
            photo = Photo(url=url, jersey_id=jersey_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', jersey_id=jersey_id)
