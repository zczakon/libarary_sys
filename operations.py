import datetime
from domain_objects import Student, Book, BookLending
import db_bind


class StudentOperations:
    Session = db_bind.sessionmaker(bind=db_bind.engine)
    session = Session()

    def __init__(self, data_repository):
        self.data_repository = data_repository

    def add(self, name, pesel, surname):
        student = Student(name, surname, pesel).create()
        self.session.add(student)
        self.session.commit()
        pass

    def list(self):
        return self.data_repository.student_list()

    def delete(self, to_delete):
        self.session.delete(to_delete)
        self.session.commit()
        pass

    def search(self, data):  # TODO remove duplicates?
        result = self.search_by_pesel(data) + self.search_by_name(data) \
                 + self.search_by_surname(data) + self.search_by_fullname(data) + self.search_by_id(data)
        return result

    def search_by_pesel(self, pesel):
        student_list = self.list()
        search_result = [student for student in student_list if student.pesel == pesel]
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

    def set_name(self, new_name, student):
        student.name = new_name
        self.session.commit()

    def set_surname(self, new_name, student):
        student.surname = new_name
        self.session.commit()

    def set_pesel(self, new_pesel, student):
        student.pesel = new_pesel
        self.session.commit()


class BookOperations:
    Session = db_bind.sessionmaker(bind=db_bind.engine)
    session = Session()

    def __init__(self, data_repository):
        self.data_repository = data_repository

    def add(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.session.add(book)
        self.session.commit()

    def list(self):
        return self.data_repository.book_list()

    def list_available(self):
        return self.data_repository.available_book_list()

    def list_pending(self):
        return self.data_repository.pending_book_list()

    def delete(self, to_delete):
        self.session.delete(to_delete)
        self.session.commit()
        pass

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

    def set_title(self, book, new_title):
        book.title = new_title
        self.session.commit()

    def set_author(self, book, new_author):
        book.author = new_author
        self.session.commit()

    def set_isbn(self, book, new_isbn):
        book.isbn = new_isbn
        self.session.commit()

    def lend_book(self, student, book):
        book_lending = BookLending(student, book).create()
        self.session.add(book_lending)
        self.session.commit()
        return book_lending

    def return_book(self, book):
        for lending in self.data_repository.lending_history:
            if lending.book == book:
                lending.set_return_date(datetime.date.today())
                self.session.commit()
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
        return self.data_repository.overdue_book_lendings_list()

    def list(self):
        return self.data_repository.lending_history()

    @staticmethod
    def check_rental_time(book_lending):
        return book_lending.rental_time()

    @staticmethod
    def check_remaining_days(book_lending):
        return book_lending.remaining_days()
