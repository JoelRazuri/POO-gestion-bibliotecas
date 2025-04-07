# Clase Prestamo
class Loan():
    def __init__(self, id_loan, book, user, date_loan, date_return):
        self.id_loan = id_loan
        self.book = book
        self.user = user
        self.date_loan = date_loan
        self.date_return = date_return
    
    def finish_loan(self):
        print(f"""
            Prestamo del libro {self.book.title} finalizado.
            Debe ser devuelto por {self.user.name} antes de {self.date_return}.
            """)