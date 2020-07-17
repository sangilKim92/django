from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),

    path('add/', views.BookmarkCreateView.as_view(), name="add",),
    path('change/', views.BookmarkChangeLV.as_view(), name="change",),
    path('update/<int:pk>', views.BookmarkUpdateView.as_view(), name="update",),
    path('delete/<int:pk>', views.BookmarkDeleteView.as_view(), name="delete",),

]