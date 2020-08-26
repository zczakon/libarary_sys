from pony.orm import *

from domain_objects import Student, Book, BookLending

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


class DataRepository:
    @staticmethod
    def get_student_list():
        student_list = select(student for student in Student.select())[:]
        return student_list

    @staticmethod
    def get_book_list():
        book_list = select(book for book in Book.select())[:]
        return book_list

    @staticmethod
    def get_lending_history():
        lending_history = select(lending for lending in BookLending.select())[:]
        return lending_history

    @staticmethod
    def lendings_per_student(student):
        student_lendings = select(lending for lending in BookLending.select() if lending.student == student)[:]
        return student_lendings

    @staticmethod
    def lendings_per_book(book):
        books_lendings = select(lending for lending in BookLending.select() if lending.book == book)[:]
        return books_lendings

    @staticmethod
    def pending_book_list():
        pending = select(lending.book for lending in BookLending.select() if lending.return_date is None)[:]
        return pending

    def available_book_list(self):
        available = select(book for book in Book.select() if self.is_lent(book) is False)[:]
        return available

    @staticmethod
    def overdue_book_list():
        overdue_lendings = select(lending for lending in BookLending.select() if lending.is_overdue())[:]
        return overdue_lendings

    def is_lent(self, book):
        lending_history = self.get_lending_history()
        for lending in lending_history:
            if lending.book == book and lending.return_date is None:
                return True
        return False
