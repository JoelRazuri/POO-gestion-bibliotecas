from classes.book import Book
from classes.librarian import Librarian
from classes.library import Library
from classes.loan import Loan
from classes.user import User

# Creando biblioteca
library = Library('Biblioteca del Pueblo')


# Creando Libros
book_1 = Book('El Señor de los Anillos', 'J.R.R. Tolkien', '11345697', 'HarperCollins', 1954, True)
book_2 = Book('Harry Potter y La piedra Filosofal', 'J.K. Rowling', '11542398', 'Bloomsbury', 1997, True)
book_3 = Book('Sinsajo', 'Suzanne Collins', '11590345', 'Scholastic', 2010, True)

print()
# Creando usuarios
user_1 = User(1, 'Joel', 'joel@joel.com')
user_2 = User(2, 'Sol', 'sol@sol.com')
user_3 = User(3, 'Marcelo', 'marcelo@marcelo.com')

# Creando bibliotecario
librarian = Librarian(1, 'Jonas')

# Ingresando usuarios
library.add_user(user_1)
library.add_user(user_2)
library.add_user(user_3)
print()
# Ingresando bibliotecario
library.add_librarian(librarian)
print()
# Mostrando usuarios
library.lists_users()
print()
# Mostrando bibliotecario
library.lists_librarians()
print()
# El bibliotecario carga los libros al sistemas
librarian.add_book(library, book_1)
librarian.add_book(library, book_2)
librarian.add_book(library, book_3)
print()
# Usuarios pidiendo prestado libros
user_1.lend_book(book_1)
user_2.lend_book(book_3)
user_3.lend_book(book_1)
print()
# Como no está disponible el libro 1, el usuario 3 pido el libro 2
user_3.lend_book(book_2)
print()
# Usuarios devuelven libros
user_1.return_book(book_1)
user_2.return_book(book_3)
user_3.return_book(book_2)
print()
# Biblitecario elimina un libro
librarian.delete_book(library, book_2)
print()
# Biblioteca elimina un usuario que no va a asistir más
library.delete_user(user_3)