# Clase Biblioteca
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        self.librarians = []

    def add_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} fue registrado en el sistema.')
    
    def delete_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f'El usuario {user.name} fue eliminado del sistema')
        else:
            print(f'El usuario {user.name} no se encuentra en el sistema.')

    def add_librarian(self, librarian):
        self.users.append(librarian)
        print(f'El bibliotecario {librarian.name} fue registrado en el sistema.')
    
    def delete_librarian(self, librarian):
        if librarian in self.users:
            self.users.remove(librarian)
            print(f'El bibliotecario {librarian.name} fue eliminado del sistema')
        else:
            print(f'El bibliotecario {librarian.name} no se encuentra en el sistema.')

    def list_books(self):
        print('LIBROS:')
        print('--------------')
        for book in self.books:
            print('#######')
            print(book)
            print('#######')
    
    def lists_useres(self):
        print('Lista Usuarios:')
        print('--------------')
        for user in self.users:
            print(f'Nombre: {user.name}, Email: {user.email}')

    def lists_librarians(self):
        print('Lista Bibliotecarios:')
        print('--------------')
        for librarian in self.librarians:
            print(f'Nombre: {librarian.name}')