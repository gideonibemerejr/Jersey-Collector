from django.urls import path
from . import views

urlpatterns = [
    # main urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jerseys/', views.jerseys_index, name='index'),
    path('jerseys/<int:jersey_id>/', views.jerseys_detail, name='detail'),
    path('jerseys/create/', views.JerseyCreate.as_view(), name="jerseys_create"),
    path('jerseys/<int:pk>/update/', views.JerseyUpdate.as_view(), name="jerseys_update"),
    path('jerseys/<int:pk>/delete/', views.JerseyDelete.as_view(), name="jerseys_delete"),
    path('jerseys/<int:jersey_id>/add_photo/', views.add_photo, name='add_photo'),
    # Teammate URLS (M:M)
    path('jerseys/<int:jersey_id>/assoc_toy/<int:teammate_id>/', views.assoc_teammate, name='assoc_teammate'),
    path('jerseys/<int:jersey_id>/unassoc_teammate/<int:teammate_id>/', views.unassoc_teammate, name='unassoc_teammate'),

    path('teammates/', views.TeammateList.as_view(), name='teammates_index'),
    path('teammates/<int:pk>/', views.TeammateDetail.as_view(), name='teammates_detail'),

    # Teammate CRUD URLS (M:M)
    path('teammates/create/', views.TeammateCreate.as_view(), name='teammates_create'),
    path('teammates/<int:pk>/update/', views.TeammateUpdate.as_view(), name='teammates_update'),
    path('teammates/<int:pk>/delete/', views.TeammateDelete.as_view(), name='teammates_delete'),
    path('accounts/signup', views.signup, name='signup'),

   
]
