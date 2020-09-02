from domain_objects import Student, Book, BookLending
from pony.orm import *

# from pony.orm import *


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
    def lendings_per_student(self):
        return Student.book_lendings.select()[:]

    @db_session
    def lendings_per_book(self):
        return Book.book_lendings.select()[:]

    @db_session
    def pending_book_list(self):
        return BookLending.select(lambda x: x.return_date is None)[:]

    @db_session
    def available_book_list(self):
        return Book.select(lambda x: not x.book_lendings)[:]
