from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('jerseys/', views.jerseys_index, name='jerseys'),
    path('jerseys/<int:jersey_id>/', views.jerseys_detail, name='detail'),
]
