from django.urls import path
from . import views

app_name ='booklib'
urlpatterns = [
    path('', views.BookView, name = 'books'),
    path('author/', views.author, name = 'author'),
    path('publisher/', views.publisher, name = 'publisher'),
]