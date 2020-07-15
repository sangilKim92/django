"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bookmark.views import BookmarkLV, BookmarkDV
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.urls import path, include
from mysite.views import HomeView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/', include('bookmark.urls')),

    path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),

    #여기다가 모든 주소를 할당하긴 너무나 어려우니 프로젝트 단위로 할당한 후 프로젝트 안에서 나머지를 할당한다.
    path('blog',include('blog.urls'))
]
