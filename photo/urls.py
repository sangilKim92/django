from django.urls import path
from photo import views
from django.views.generic import ListView, DetailView

from photo.models import Album, Photo
app_name = 'photo'

urlpatterns = [
    path('', ListView.as_view(model=Album), name='index'),

    path('', ListView.as_view(model=Album), name='index'),

    path('album/<int:pk>', ListView.as_view(model=Album), name='album_list'),

    path('photo/<int:pk>/', DetailView.as_view(), name='photo_detail'),
]