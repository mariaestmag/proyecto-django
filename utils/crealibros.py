from catalogo.models import Book

for n in range(10): ##Esto creará un rango de 10 libros con ese título y sus diferentes numeraciones
    b = Book(title=f'Libro de prueba {n}')
    b.save() ##guarda y commit en bbdd