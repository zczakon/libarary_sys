from library_components import Student, Book
from data_source import DataRepository
# TODO zrobić by Operations nie printowało list - raczej nie powinien, bo to nie interface. Zwracanie?


class StudentOperations:
    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository

    def add(self, name, pesel, surname):
        student = Student(name, surname, pesel)
        self.data_repository.add_student(student)
        return student

    def list(self):
        return self.data_repository.get_student_list()

    def delete(self, student_name_surname):
        to_delete = self.search(student_name_surname)
        self.data_repository.delete_student(to_delete)
        pass

    def search(self, data):
        student_list = self.list()
        for student in student_list:
            if student.full_name in self.search_by_fullname(data):
                return student
            elif student.surname in self.search_by_surname(data):
                return student
            elif student.pesel == data:
                return student
            elif student.id == data:
                return student
            else:
                pass

    def search_by_fullname(self, student_full_name: str):
        search_results = []
        student_list = self.list()
        for student in student_list:
            if (student.name + ' ' + student.surname) == student_full_name:
                search_results.append(student)
        return search_results

    def search_by_surname(self, surname):
        search_results = []
        student_list = self.list()
        for student in student_list:
            if student.surname == surname:
                search_results.append(student)
        return search_results

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

    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository

    def add(self, author, isbn, title):
        book = Book(isbn, title, author)
        self.data_repository.add_book(book)

    def list(self):
        return self.data_repository.get_book_list()

    def list_available(self):
        return self.data_repository.get_available_book_list()

    def delete(self, title):
        to_delete = self.search(title)
        self.data_repository.delete_book(to_delete)
        pass

    def search(self, data):
        book_list = self.list()
        for book in book_list:
            if book in self.search_by_title(data):
                return book
            elif book in self.search_by_author(data):
                return book
            elif book in self.search_by_isbn(data):
                return book
            elif book.id == data:
                return book
            else:
                pass

    def search_by_title(self, title):
        search_results = []
        for book in self.list():
            if book.title == title:
                search_results.append(book)
        return search_results

    def search_by_author(self, author):
        search_results = []
        for book in self.list():
            if book.author == author:
                search_results.append(book)
        return search_results

    def search_by_isbn(self, isbn):
        search_results = []
        for book in self.list():
            if book.isbn == isbn:
                search_results.append(book)
        return search_results

    @staticmethod
    def set_title(book, new_title):
        book.set_title(new_title)

    @staticmethod
    def set_author(book, new_author):
        book.set_author(new_author)

    @staticmethod
    def set_isbn(book, new_isbn):
        book.set_isbn(new_isbn)

    def is_available(self, to_lend):
        available_book_list = self.list_available()
        if to_lend in available_book_list:
            return True
        pass


class BookLendingOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def search(self):
        pass

    def search_by_student(self, student):
        return self.data_repository.lendings_per_student(student)

    def search_by_book(self, book):
        return self.data_repository.lendings_per_book(book)

    def see_overdue(self):
        lending_history = self.data_repository.get_lending_history()
        return self.data_repository.overdue_book_list(lending_history)

    def list(self):
        return self.data_repository.get_lending_history()

    def flatten_lending_history(self):
        lending_history = self.list()
        flat_list = []
        for sublist in lending_history:
            for item in sublist:
                flat_list.append(item)
        print(flat_list)
        return flat_list

    @staticmethod
    def check_rental_time(book_lending):
        return book_lending.rental_time()

    @staticmethod
    def check_remaining_days(book_lending):
        return book_lending.remaining_days()
