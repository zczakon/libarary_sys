import datetime

from sqlalchemy.orm import relationship

from accounts import Account, Role
import db_bind
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


class Student(db_bind.Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    pesel = Column(String)
    registration_date = Column(DateTime)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    lending_id = Column(Integer, ForeignKey('lendings.id'))

    account = relationship("Account", back_populates="student")
    lendings = relationship("BookLending", back_populates="student")

    def __str__(self):
        return '({}, {}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                         'ID:' + str(self.id), 'role: ' + str(self.account.get_role()))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.name + ' ' + self.surname, 'PESEL: ' + str(self.pesel),
                                         'ID:' + str(self.id), 'role: ' + str(self.account.get_role()))

    def __eq__(self, other):
        pass

    def create(self):
        self.registration_date = datetime.date.today()
        return self

    def create_account(self):
        self.account = Account(Role(name="user"))
        return self

    def fullname(self):
        return str(self.name) + ' ' + str(self.surname)


class Book(db_bind.Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    lending_id = Column(Integer, ForeignKey('lendings.id'))

    lendings = relationship("BookLending", back_populates="book")

    def __str__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(str(self.title), 'author: ' + self.author, 'ISBN: ' +
                                         str(self.isbn), 'ID: ' + str(self.id))


class BookLending(db_bind.Base):
    __tablename__ = 'lendings'

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime)
    max_return_date = Column(DateTime)
    return_date = Column(DateTime)
    student_id = Column(Integer, ForeignKey('students.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    student = relationship("Student", back_populates="lendings")
    book = relationship("Book", back_populates="lendings")

    return_time = 30

    def __str__(self):
        return '({}, {}, {}, {})'.format(str(self.book), str(self.student), 'creation date: '
                                         + str(self.creation_date), 'return date: ' +
                                         str(self.return_date))

    def __repr__(self):
        return '({}, {}, {}, {})'.format(str(self.book), str(self.student), 'creation date :'
                                         + str(self.creation_date), 'return date: ' +
                                         str(self.return_date))

    def create(self):
        self.creation_date = datetime.date.today()
        self.max_return_date=self.creation_date + datetime.timedelta(days=self.return_time)
        return self

    def is_overdue(self):
        if self.return_date is None:
            return datetime.date.today() > self.max_return_date

    def rental_time(self):
        return datetime.date.today() - self.creation_date

    def remaining_days(self):
        if self.return_date is None:
            pass
        return self.max_return_date - self.max_return_date
