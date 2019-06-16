from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('jerseys/', views.jerseys_index, name='jerseys'),
    path('jerseys/<int:jersey_id>/', views.jerseys_detail, name='detail'),
    path('jerseys/create/', views.JerseyCreate.as_view(), name="jerseys_create"),
    path('jerseys/<int:pk>/update/', views.JerseyUpdate.as_view(), name="jerseys_update"),
    path('jerseys/<int:pk>/delete/', views.JerseyDelete.as_view(), name="jerseys_delete"),
    path('jerseys/<int:jersey_id>/add_teammate/', views.add_teammate, name='add_teammate' )
]
