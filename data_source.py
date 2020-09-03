import datetime

from domain_objects import Student, Book, BookLending
from pony.orm import *


class SqlDataRepository:
    @db_session
    def student_list(self):
        return Student.select()[:]

    @db_session
    def book_list(self):
        return Book.select()[:]

    @db_session
    def lending_history(self):
        return BookLending.select()[:]

    @db_session
    def lendings_per_student(self, student_id):  # TODO fix
        student = Student.get(id=student_id)
        return list(student.book_lendings)

    @db_session
    def lendings_per_book(self, book_id):  # TODO fix
        book = Book.get(id=book_id)
        return list(book.book_lendings)

    @db_session
    def pending_book_list(self):
        # pending_lendings = BookLending.select(lambda x: x.return_date is None)[:]
        return select(lending.book for lending in BookLending if lending.return_date is None)[:]

    @db_session
    def available_book_list(self):
        return Book.select(lambda x: not x.book_lendings)[:]

    @db_session
    def overdue_book_list(self):
        return BookLending.select(lambda x: x.return_date is None and datetime.date.today() > x.max_return_date)[:]
