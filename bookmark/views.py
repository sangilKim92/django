from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):
    model = Bookmark

#리스트뷰를 상속하고 사용할 모델만 저장시켰다.

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner= self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')