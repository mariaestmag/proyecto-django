'''
0. Recuerda añadir app a installed apps en settings.py
1. Definir modelos
2. python manage.py migrate
'''
from django.db import models
from django.db.models.base import Model
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField("Género",max_length=200)

    def __str__(self): #los métodos van SIEMPRE con self
         return self.name

class Author(models.Model):
    first_name = models.CharField('Nombre',max_length=100)
    last_name = models.CharField('Apellido',max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Muerte', null=True, blank=True)

    #ponemos NULL=True cuando los datos son "especiales" y necesitan tener algún valor

    def __str__(self):
        return self.first_name
        
        
class Book(models.Model):
    '''Libro para aplicación de bibioteca...'''
    title = models.CharField(max_length=250)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, blank=True) #si alguno de los campos puede estar vacío, hay que poner blank a true
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Autor') #AQUÍ NO TOCAMOS AUTHOR aunque queramos poner Autor de etiqueta
    fecha = models.DateField(blank=True, null=True,help_text='Fecha de publicacion') #auto_now lo ponemos para que coja una fecha por cada introducción de dato

    # Al tratarse de un campo como clave foránea, para mantener la integridad (on delete) establecemos null true
    # para que, aunque vayamos a crear un libro (si aún no está ese autor), siempre sea posible y se mantenga la integridad referencial.
    
    genre = models.ManyToManyField(Genre)

    def __str__(self): #Cuando hacemos print o mostramos un objeto, tira de este método
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def muestra_genero(self):
        '''Muestra genero para admin'''
        return ', '.join([gen.name for gen in self.genre.all()]) #recorre todos los géneros que tenga un libro

        #[gen.name for gen in self.genre.all()[:3]]) aquí sacaría solo los 3 primeros

    muestra_genero.short_description = 'Género'

    class Meta:
        verbose_name = 'Libro'