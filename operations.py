import datetime
from pony.orm import db_session
from domain_objects import Student, Book, BookLending


class StudentOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    @db_session
    def add(self, name, pesel, surname):
        student = Student(name, surname, pesel)
        student.create_account()
        return student

    @db_session
    def delete_student(self, student):
        student.delete()
        pass

    def list(self):
        return self.data_repository.get_student_list()

    def search(self, data):
        result = self.search_by_pesel(data) + self.search_by_name(data) \
                 + self.search_by_surname(data) + self.search_by_fullname(data) + self.search_by_id(data)
        return result

    def search_by_pesel(self, pesel):
        student_list = self.list()
        # print('student list', student_list)  # remove
        search_result = [student for student in student_list if student.pesel == pesel]
        # print('search result by pesel: ', search_result)  # remove
        return search_result

    def search_by_fullname(self, fullname):
        student_list = self.list()
        search_result = [student for student in student_list if student.fullname == fullname]
        return search_result

    def search_by_surname(self, surname):
        student_list = self.list()
        search_result = [student for student in student_list if student.surname == surname]
        return search_result

    def search_by_name(self, name):
        student_list = self.list()
        search_result = [student for student in student_list if student.name == name]
        return search_result

    def search_by_id(self, student_id):
        student_list = self.list()
        search_result = [student for student in student_list if student.id == student_id]
        return search_result

    @staticmethod
    @db_session
    def set_name(new_name, student):
        student.set_name(new_name)
        pass

    @staticmethod
    @db_session
    def set_surname(new_name, student):
        student.set_surname(new_name)
        pass

    @staticmethod
    @db_session
    def set_pesel(new_pesel, student):
        student.set_pesel(new_pesel)


class BookOperations:

    def __init__(self, data_repository):
        self.data_repository = data_repository

    @db_session
    def add(self, title, author, isbn):
        book = Book(title, author, isbn)
        return book

    @db_session
    def delete_book(self, book):
        book.delete()

    def list(self):
        return self.data_repository.get_book_list()

    def list_available(self):
        return self.data_repository.available_book_list()

    def list_pending(self):
        return self.data_repository.pending_book_list()

    def search(self, data):
        result = self.search_by_title(data) + self.search_by_author(data) + self.search_by_isbn(data) + \
                 self.search_by_id(data)
        return result

    def search_by_id(self, book_id):
        book_list = self.list()
        search_result = [book for book in book_list if book.id == book_id]
        return search_result

    def search_by_title(self, title):
        book_list = self.list()
        search_result = [book for book in book_list if book.title == title]
        return search_result

    def search_by_author(self, author):
        book_list = self.list()
        search_result = [book for book in book_list if book.author == author]
        return search_result

    def search_by_isbn(self, isbn):
        book_list = self.list()
        search_result = [book for book in book_list if book.isbn == isbn]
        return search_result

    @staticmethod
    @db_session
    def set_title(book, new_title):
        book.set_title(new_title)

    @staticmethod
    @db_session
    def set_author(book, new_author):
        book.set_author(new_author)

    @staticmethod
    @db_session
    def set_isbn(book, new_isbn):
        book.set_isbn(new_isbn)

    @db_session
    def lend_book(self, student, book):
        book_lending = BookLending(student, book).create()
        self.data_repository.lending_history.append(book_lending)
        return book_lending

    @db_session
    def return_book(self, book):
        for lending in self.data_repository.lending_history:
            if lending.book == book:
                lending.set_return_date(datetime.date.today())
                pass


class BookLendingOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def search(self, data):
        result = self.search_by_student(data) + self.search_by_book(data)
        return result

    def search_by_student(self, student):
        print('search_by_student in operations:', self.data_repository.lendings_per_student(student))
        return self.data_repository.lendings_per_student(student)

    def search_by_book(self, book):
        return self.data_repository.lendings_per_book(book)

    def list_overdue(self):
        return self.data_repository.overdue_book_list()

    def list(self):
        return self.data_repository.get_lending_history()

    @staticmethod
    def check_rental_time(book_lending):
        return book_lending.rental_time()

    @staticmethod
    def check_remaining_days(book_lending):
        return book_lending.remaining_days()
