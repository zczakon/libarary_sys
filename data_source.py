from domain_objects import Student, Book, BookLending
# from pony.orm import *


class SqlDataRepository:
    @staticmethod
    def student_list():
        return Student.select()[:]

    @staticmethod
    def book_list():
        return Book.select()[:]

    @staticmethod
    def lending_history():
        return BookLending.select()[:]

    @staticmethod
    def lendings_per_student():
        return Student.book_lendings.select()[:]

    @staticmethod
    def lendings_per_book():
        return Book.book_lendings.select()[:]

    @staticmethod
    def pending_book_list():
        return BookLending.select(lambda x: x.return_date is None)[:]

    @staticmethod
    def overdue_book_list():
        return BookLending.select(lambda x: x.is_overdue())[:]

    def available_book_list(self):
        return Book.select(lambda x: self.is_lent(x))[:]

    def is_lent(self, book):
        lending_history = self.lending_history()
        for lending in lending_history:
            if lending.book == book and lending.return_date is None:
                return True
        return False
