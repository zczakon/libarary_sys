from datetime import datetime

import db_bind
from domain_objects import Student, Book, BookLending


class SqlDataRepository:
    Session = db_bind.sessionmaker(bind=db_bind.engine)
    session = Session()

    def student_list(self):
        query = self.session.query(Student)
        return query.all()

    def book_list(self):
        query = self.session.query(Book)
        return query.all()

    def lending_list(self):
        query = self.session.query(BookLending)
        return query.all()

    def lendings_per_student(self, student):
        query = self.session.query(BookLending).filter(BookLending.student == student)
        return query.all()

    def lendings_per_book(self, book):
        query = self.session.query(BookLending).filter(BookLending.book == book)
        return query.all()

    def pending_book_list(self):
        query = self.session.query(BookLending.book).filter(BookLending.is_(None))
        return query.all()

    def available_book_list(self):  # ŹLE ksiazki dostepne: byla wypozyczona i zostala oddana
        query1 = self.session.query(Book).filter(Book.lendings.is_(None))
        query2 = self.session.query(Book).join(BookLending).filter.and_(Book.lendings.isnotNone,
                                                                        BookLending.return_date.isnot(None))
        return query1.all() + query2.all()

    def overdue_book_lendings_list(self):
        query = self.session.query(BookLending).filter.and_(BookLending.return_date.is_(None),
                                                            BookLending.max_return_date < datetime.date.today())
        return query.all()
