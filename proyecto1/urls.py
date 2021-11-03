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
from django import urls, views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from catalogo.views import BookDetailView, indice, BookListView #crearemos una vista indice para poder importarla y utilizarla en patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name ='indice'), # si no hay path, que meta la función que le vamos a definir nosotros para esa vista
    path('books', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
]
