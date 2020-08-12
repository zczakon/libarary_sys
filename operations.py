from classes import Student, Book
from data_source import DataRepository


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

    def search(self, student_name_surname: str):
        for student in self.list():
            if (student.name + ' ' + student.surname) == student_name_surname:
                return student


class BookOperations:

    def __init__(self, data_repository):
        self.data_repository = data_repository

    def add(self, author, isbn, title):
        book = Book(isbn, title, author)
        self.data_repository.add_book(book)

    def list(self):
        return self.data_repository.get_book_list()

    def delete(self, title):
        to_delete = self.search(title)
        self.data_repository.delete_book(to_delete)
        pass

    def search(self, title):
        for book in self.data_repository.book_list:
            if book.title == title:
                return book

    def list_available(self):
        return self.data_repository.get_available_book_list()
