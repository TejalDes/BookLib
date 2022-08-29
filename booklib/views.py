from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from .models import Books, Author, Publisher

# class BookView(generic.DetailView):
#     model = Books
#     template_name: 'booklib/books.html'


def BookView(request):
    books_list = Books.objects.all()
    context = {'books_list' : books_list}
    return render(request, 'booklib/books.html', context)

def author(request):
    author_list = Author.objects.all()
    context = {'author_list' : author_list}
    return render(request, 'booklib/author.html', context)

def publisher(request):
    publisher_list = Publisher.objects.all()
    context = {'publisher_list' : publisher_list}
    return render(request, 'booklib/publisher.html', context)
