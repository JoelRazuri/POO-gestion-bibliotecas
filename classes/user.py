# Clase Usuario
class User():
    def __init__(self, id_user, name, email):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f""""
                Usuario: {self.name},
                Email: {self.email},
                Lista libros: {self.borrowed_books}
                """

    def lend_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.update_available(False)
            print(f'Libro {book.title} prestado a {self.name}.')
        else:
            print('Este libro no está disponible para préstamo.')

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_available(True)
            print(f'Libro {book.title} devuelto por {self.name}')