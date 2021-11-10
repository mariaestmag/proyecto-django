from django.shortcuts import render,redirect #coge una plantilla y la devuelve
from django.views import generic
from catalogo.models import Author, Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from catalogo.forms import AuthorForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#from django.http import HttpResponse

# Create your views here.

def indice(request): #las funciones siempre tienen compo parámetro un request, una petición
    '''
    Página inicial de nuestra web
    '''

    datos = {'autor':'Luis Miguel'}
    busqueda = request.GET.get('q') #lanzaremos sobre mis libros para ver cuál tienen esa palabra
    if busqueda: 
        libros = Book.objects.filter(title__icontains=busqueda)
    else: #si GET es falso (none) entonces sigue con lo que había
        libros = Book.objects.all()

    datos ['libros'] = libros 
    return render(request, 'index.html', context=datos) #y siempre hay que responder con algo, una plantilla por lo general

def contacto(request): #las funciones siempre tienen compo parámetro un request, una petición
    '''
    Página de contacto de nuestra web
    '''
    return render(request, 'contacto.html')

#TODO LO QUE TIENE QUE VER CON LIBRO

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5
 
class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book
    template_name = 'book_detail.html'

#TODO LO QUE TIENE QUE VER CON AUTOR

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors_list.html'
    queryset = Author.objects.all().order_by('last_name', 'first_name')

 
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Autor creado.')
            return redirect('/')
    else:
        form = AuthorForm()
    datos = {'form': AuthorForm()}
    return render(request, 'create_author.html', 
        context=datos)

# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModifyAuthor(SuccessMessageMixin, generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'modify_author.html'
    success_url = '/'
    success_message = "%(first_name)s %(last_name)s se ha modificado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class DeleteAuthor(SuccessMessageMixin, generic.DeleteView):
    model = Author
    template_name = 'delete_author.html'
    success_url = '/'
    success_message = "El autor se ha borrado correctamente"

    def delete(self,request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(DeleteAuthor, self).delete(request, *args, **kwargs)

#Este search es mío
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'search.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if not query:
            query=""
        else:
            return Book.objects.filter(title__icontains=query)
    


