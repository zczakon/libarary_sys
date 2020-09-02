import datetime

from accounts import Account, Role
from data_source import db
from pony.orm import Required, Optional, Set


class Student(db.Entity):
    name = Required(str)
    surname = Required(str)
    pesel = Required(str)
    registration_date = Optional(datetime.date)
    account = Optional(Account)
    book_lendings = Set('BookLending')

    def fullname(self):
        return str(self.name) + ' ' + str(self.surname)

    def create_account(self):
        self.account = Account(Role(name="user"))

    def create(self):
        self.registration_date = datetime.date.today()

    def __str__(self):
        return '({}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                     'ID:' + str(self.id)), 'role: ' + str(self.account.get_role())

    def __repr__(self):
        return '({}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                     'ID:' + str(self.id)), 'role: ' + str(self.account.get_role())


class Book(db.Entity):
    isbn = Required(str)
    title = Required(str)
    author = Required(str)
    book_lendings = Set('BookLending')

    def __str__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))


class BookLending(db.Entity):
    student = Required(Student)
    book = Required(Book)
    creation_date = Required(datetime.datetime)
    max_return_date = Required(datetime.datetime)
    return_date = Optional(datetime.datetime)

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


db.generate_mapping(create_tables=True)
