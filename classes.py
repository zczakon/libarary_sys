import datetime
import random
import string
from datetime import timedelta
from typing import List


class Student:
    books_lent: List

    def __init__(self, name: str, surname: str, pesel: int):
        assert isinstance(name, str)
        self.name = name
        assert isinstance(surname, str)
        self.surname = surname
        self.pesel = pesel
        self.id = id(self)
        self.account = Account(generate_pass(6), Role("user"))
        self.reg_date = datetime.date.today()
        self.books_lent = []

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
        self.books_lent.append(BookLending(self, book))
        pass

    def return_book(self, book):
        """
        deletes from books_lent list the book
        """
        for lending in self.books_lent:
            if lending.book == book:
                self.books_lent.remove(lending)
        pass


class Role:
    def __init__(self, name):
        self.name = name
        self.id = id(self)

    def get_name(self):
        return self.name


class Account:
    def __init__(self, password: str, role: Role):
        self.password = password
        self.role = role
        self.id = id(self)

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_id(self):
        return self.id

    def set_password(self, new_password):
        self.password = new_password

    def change_password(self, new_password):
        self.set_password(new_password)
        pass


class Book:
    def __init__(self, isbn: int, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.id = id(self)

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id


class BookLending:
    return_time = 30

    def __init__(self, student: Student, book: Book):
        self.student = student
        self.book = book
        self.id = id(self)
        self.creation_date = datetime.date.today()
        self.return_date = datetime.date.today() + timedelta(days=self.return_time)

    def is_overdue(self):
        return datetime.date.today() > self.return_date

    def get_student(self):
        return self.student

    def get_book(self):
        return self.book

    def get_id(self):
        return self.id

    def get_creation_date(self):
        return self.creation_date

    def get_return_date(self):
        return self.return_date


def generate_pass(n: int) -> str:
    return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(n)))


class Lists:
    def __init__(self):
        self.student_list = []
        self.book_list = []

    def add_student(self, student):
        self.student_list.append(student)
        pass

    def del_student(self, student):
        self.student_list.remove(student)
        pass

    def add_book(self, book):
        self.book_list.append(book)
        pass

    def del_book(self, book):
        self.book_list.remove(book)
        pass

    def get_student_list(self):
        return self.student_list

    def get_book_list(self):
        return self.book_list
