import datetime
from pony.orm import db_session
from domain_objects import Student, Book, BookLending


class StudentOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    @db_session
    def add(self, name, pesel, surname):
        student = Student(name=name, surname=surname, pesel=pesel)
        student.create_account()
        return student

    @db_session
    def delete_student(self, student):
        student.delete()
        pass

    def list(self):
        return self.data_repository.student_list()

    def search(self, data):
        return self.search_by_pesel(data) + self.search_by_name(data) \
               + self.search_by_surname(data) + self.search_by_fullname(data)

    @db_session
    def search_by_pesel(self, pesel):
        return Student.select(lambda x: x.pesel == pesel)[:]

    @db_session
    def search_by_fullname(self, fullname):
        return Student.select(lambda x: x.fullname() == fullname)[:]

    @db_session
    def search_by_name(self, name):
        return Student.select(lambda x: x.name == name)[:]

    @db_session
    def search_by_surname(self, surname):
        return Student.select(lambda x: x.surname == surname)[:]

    @db_session
    def set_name(self, new_name, student):
        student.name = new_name
        pass

    @db_session
    def set_surname(self, new_surname, student):
        student.surname = new_surname

    @db_session
    def set_pesel(self, new_pesel, student):
        student.pesel = new_pesel


class BookOperations:

    def __init__(self, data_repository):
        self.data_repository = data_repository

    @db_session
    def add(self, title, author, isbn):
        book = Book(title=title, author=author, isbn=isbn)
        return book

    @db_session
    def delete_book(self, book):
        book.delete()

    def list(self):
        return self.data_repository.book_list()

    def list_available(self):
        return self.data_repository.available_book_list()

    def list_pending(self):
        return self.data_repository.pending_book_list()

    def search(self, data):
        return self.search_by_title(data) + self.search_by_author(data) + self.search_by_isbn(data)

    @db_session
    def search_by_title(self, title):
        return Book.select(lambda x: x.title == title)[:]

    @db_session
    def search_by_author(self, author):
        return Book.select(lambda x: x.author == author)[:]

    @db_session
    def search_by_isbn(self, isbn):
        return Book.select(lambda x: x.isbn == isbn)[:]

    @db_session
    def set_title(self, book, new_title):
        book.title = new_title

    @db_session
    def set_author(self, book, new_author):
        book.author = new_author

    @db_session
    def set_isbn(self, book, new_isbn):
        book.isbn = new_isbn

    @db_session
    def lend_book(self, student_id, book_id):
        student = Student.get(id=student_id)
        book = Book.get(id=book_id)
        book_lending = BookLending(student=student, book=book).create()
        return book_lending

    @db_session
    def return_book(self, book_id):
        book = Book.get(id=book_id)
        for lending in self.data_repository.lending_history():
            if lending.book == book:
                lending.return_date = datetime.date.today()
                pass


class BookLendingOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def search(self, data):
        return self.search_by_student(data) + self.search_by_book(data)

    def search_by_student(self, student):
        return self.data_repository.lendings_per_student(student)

    def search_by_book(self, book):
        return self.data_repository.lendings_per_book(book)

    def list_overdue(self):
        return self.data_repository.overdue_book_list()

    def list(self):
        return self.data_repository.lending_history

    @staticmethod
    def check_rental_time(book_lending):
        return book_lending.rental_time()

    @staticmethod
    def check_remaining_days(book_lending):
        return book_lending.remaining_days()
