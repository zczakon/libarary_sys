import datetime

import data_source
from accounts import Account, Role  # TODO make method creating student acc
from pony.orm import *


class Student(data_source.db.Entity):
    name = Required(str)
    surname = Required(str)
    pesel = Required(str, unique=True)
    registration_date = Required(datetime)
    account = Optional(Account)

    fullname = str(name) + ' ' + str(surname)

    def create_account(self):
        self.account = Account(Role("user"))

    def __str__(self):
        return '({}, {}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                         'ID:' + str(self.id), 'role: ' + str(self.account.get_role()))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                         'ID:' + str(self.id), 'role: ' + str(self.account.get_role()))

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_pesel(self):
        return self.pesel

    def get_id(self):
        return self.id

    def get_reg_date(self):
        return self.registration_date

    def set_name(self, new_name):
        self.name = new_name

    def set_surname(self, new_surname):
        self.surname = new_surname

    def set_pesel(self, new_pesel):
        self.pesel = new_pesel


class Book(data_source.db.Entity):
    isbn = Required(str)
    title = Required(str)
    author = Required(str)

    def __str__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id

    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn


class BookLending(data_source.db.Entity):
    student = Required(Student)
    book = Required(Book)
    creation_date = Required(datetime)
    max_return_date = Required(datetime)
    return_date = Optional(datetime)

    return_time = 30

    def create(self):
        self.creation_date = datetime.date.today()
        self.max_return_date = self.creation_date + datetime.timedelta(days=self.return_time)

    def __str__(self):
        return '({}, {}, {}, {})'.format(str(self.book), str(self.student), 'creation date: '
                                         + str(self.creation_date), 'return date: ' +
                                         str(self.return_date))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(str(self.book), str(self.student), 'creation date :'
                                         + str(self.creation_date), 'return date: ' +
                                         str(self.return_date))

    def is_overdue(self):
        if self.return_date is None:
            return datetime.date.today() > self.max_return_date

    def rental_time(self):
        return datetime.date.today() - self.creation_date

    def remaining_days(self):
        if self.return_date is None:
            pass
        return self.max_return_date - self.max_return_date

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

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date
