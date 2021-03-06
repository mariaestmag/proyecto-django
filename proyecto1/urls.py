"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.urls import include, path
from django import urls, views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from catalogo.views import AuthorDetailView, AuthorListView, BookDetailView, DeleteAuthor, ModifyAuthor, indice, BookListView,contacto,SearchResultsListView,create_author,ModifyAuthor, DeleteAuthor #crearemos una vista indice para poder importarla y utilizarla en patterns

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', indice, name ='indice'), # si no hay path, que meta la función que le vamos a definir nosotros para esa vista
    path('books', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create', create_author, name='create_author'),
    path('author/modify/<int:pk>', ModifyAuthor.as_view(), name='modify_author'),
    path('author/delete/<int:pk>', DeleteAuthor.as_view(), name='delete_author'),
    path('contacto', contacto, name ='contacto'),
    path('search', SearchResultsListView.as_view(), name='search'),
]
