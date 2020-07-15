from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

#리스트뷰를 상속하고 사용할 모델만 저장시켰다.

class BookmarkDV(DetailView):
    model = Bookmark