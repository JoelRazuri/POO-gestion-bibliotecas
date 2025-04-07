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
                Disponibilidad: {self.available}
                """

    def update_available(self):
        if self.available:
            self.available = False
            return self.available
        else:
            self.available = True
            return self.available

        return f"Hubo un error, intentelo de nuevo"


# Pruebas
# libro = Book('Iron Man: El primer Vengador', 'Stan Lee', 'M1827', 'Marvel Studios', '03/03/1967', True)

# print(libro)

# libro.update_available()
# print(libro)

# libro.update_available()
# print(libro)
