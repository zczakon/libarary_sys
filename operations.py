import datetime
from domain_objects import Student, Book, BookLending


class StudentOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def add(self, name, pesel, surname):
        student = Student(name, surname, pesel)
        self.data_repository.add_student(student)
        return student

    def list(self):
        return self.data_repository.get_student_list()

    def delete(self, to_delete):
        self.data_repository.delete_student(to_delete)
        pass

    def search(self, data):  # TODO remove duplicates?
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
    def set_name(new_name, student):
        student.set_name(new_name)
        pass

    @staticmethod
    def set_surname(new_name, student):
        student.set_surname(new_name)
        pass

    @staticmethod
    def set_pesel(new_pesel, student):
        student.set_pesel(new_pesel)


class BookOperations:

    def __init__(self, data_repository):
        self.data_repository = data_repository

    def add(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.data_repository.add_book(book)
        # print(self.data_repository.get_book_list())

    def list(self):
        return self.data_repository.get_book_list()

    def list_available(self):
        return self.data_repository.available_book_list()

    def list_pending(self):
        return self.data_repository.pending_book_list()

    def delete(self, to_delete):
        self.data_repository.delete_book(to_delete)
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

    @staticmethod
    def set_title(book, new_title):
        book.set_title(new_title)

    @staticmethod
    def set_author(book, new_author):
        book.set_author(new_author)

    @staticmethod
    def set_isbn(book, new_isbn):
        book.set_isbn(new_isbn)

    def lend_book(self, student, book):
        book_lending = BookLending(student, book)
        self.data_repository.lending_history.append(book_lending)
        return book_lending

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
        return result1

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
