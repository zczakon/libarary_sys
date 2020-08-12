import datetime
from datetime import timedelta
from typing import List
from accounts import Account, Role


class Student:
    books_lent: List

    def __init__(self, name: str, surname: str, pesel: int):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(surname, str)
        self.surname = surname
        self.pesel = pesel
        self.id = id(self)
        self.account = Account(Role("user"))
        self.reg_date = datetime.date.today()
        self.lendings = []

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_pesel(self):
        return self.pesel

    def get_id(self):
        return self.id

    def get_account(self):
        return self.account

    def get_reg_date(self):
        return self.reg_date

    def get_books_lent(self):
        return self.books_lent

    def lend_book(self, book):
        """
        returns BookLending instance
        """
        self.lendings.append(BookLending(self, book))
        pass

    def return_book(self, book):
        """
        deletes from books_lent list the book
        """
        for lending in self.lendings:
            if lending.book == book:
                lending.set_return_date(datetime.date.today())
        pass


class Book:
    def __init__(self, isbn: int, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.id = id(self)

    def __str__(self):
        return '"'+str(self.title)+'"'

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id


class BookLending:
    id: int
    return_date: datetime
    return_time = 30

    def __init__(self, student: Student, book: Book):
        self.student = student
        self.book = book
        self.id = id(self)
        self.creation_date = datetime.date.today()
        self.max_return_date = datetime.date.today() + timedelta(days=self.return_time)
        self.return_date = None

    def __str__(self):
        return str(self.book), str(self.student), 'creation date :' + str(self.creation_date),\
               'return date: ' + str(self.return_date)

    def is_overdue(self):
        if self.return_date is not None:
            return datetime.date.today() > self.max_return_date

    def get_student(self):
        return self.student

    def get_book(self):
        return self.book

    def get_id(self):
        return self.id

    def get_creation_date(self):
        return self.creation_date

    def get_max_return_date(self):
        return self.max_return_date

    def get_return_date(self):
        if self.return_date is not None:
            return self.return_date

    def set_return_date(self, return_date):
        self.return_date = return_date
