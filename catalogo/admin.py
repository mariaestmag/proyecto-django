from django.contrib import admin
from django.db.models import fields

# Register your models here.
from .models import Book, Author, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','muestra_genero'] #Cambia lo que se muestra en libro
    list_filter = ['author','genre'] #Añade un filtro

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #Indico cómo se ponen los campos en la pantalla de detalle
    # Entre paréntesis hace que los campos se queden en una misma línea
    fieldsets = (
        ('Datos personales',
            {'fields': ('first_name','last_name')}),
        ('Fechas',
            {'fields': ('date_of_birth','date_of_death')})
            )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass