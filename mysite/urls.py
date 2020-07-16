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

from django.conf.urls.static import static
from django.conf import settings
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    #path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/', include('bookmark.urls')),

    path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    #여기다가 모든 주소를 할당하긴 너무나 어려우니 프로젝트 단위로 할당한 후 프로젝트 안에서 나머지를 할당한다.
    path('blog',include('blog.urls')),

    path('photo/', include('photo.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
