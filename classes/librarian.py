# Clase Bibliotecario
class Librarian():
    def __init__(self, id_librarian, name):
        self.id_librarian = id_librarian
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)
        print(f'Libro {book.title} añadido al sistema.')
    
    def delete_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f'Libro {book.title} eliminado del sistema.')