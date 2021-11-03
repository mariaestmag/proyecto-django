from django.shortcuts import render #coge una plantilla y la devuelve
from django.views import generic
from catalogo.models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


#from django.http import HttpResponse

# Create your views here.

def indice(request): #las funciones siempre tienen compo parámetro un request, una petición
    '''
    Página inicial de nuestra web
    '''
    libros = Book.objects.all()

    datos = {'autor':'Luis','libros': libros}
    return render(request, 'index.html', context=datos) #y siempre hay que responder con algo, una plantilla por lo general

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    template_name = 'book_list.html'
 


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book
    template_name = 'book_detail.html'
   
