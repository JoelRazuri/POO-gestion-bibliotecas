# Clase Libro
class Book():
    def __init__(self, title, author, isbn_book, editorial, publish_date, available):
        self.title = title
        self.author = author
        self.isbn_book = isbn_book
        self.editorial = editorial
        self.publish_date = publish_date
        self.available = available

    def __str__(self):
        return f""""
                Titulo: {self.title},
                Autor : {self.author},
                ISBN: {self.isbn_book},
                Editorial: {self.editorial},
                Fecha de publicación: {self.publish_date},
                """

    def update_available(self, available):
        self.available = available
        state = 'disponible' if available else 'no disponible'
        print(f'El libro {self.title} ahora está {state}')
