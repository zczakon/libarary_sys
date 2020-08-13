from library_components import Student, Book


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
        student_list = self.data_repository.get_student_list()
        for student in student_list:
            if student.full_name in self.list_by_fullname(data):
                return student
            elif student.surname in self.list_by_surname(data):
                return student
            elif student.pesel == data:
                return student
            elif student.id == data:
                return student
            else:
                return None

    def list_by_fullname(self, student_full_name: str):
        search_results = []
        student_list = self.list()
        for student in student_list:
            if (student.name + ' ' + student.surname) == student_full_name:
                search_results.append(student)
        return search_results

    def list_by_surname(self, surname):
        search_results = []
        student_list = self.list()
        for student in student_list:
            if student.surname == surname:
                search_results.append(student)
        return search_results


class BookOperations:

    def __init__(self, data_repository):
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
            if book in self.list_by_title(data):
                return book
            elif book in self.list_by_author(data):
                return book
            elif book in self.list_by_isbn(data):
                return book
            elif book.id == data:
                return book
            else:
                return None

    def list_by_title(self, title):
        search_results = []
        for book in self.data_repository.book_list:
            if book.title == title:
                search_results.append(book)
        return search_results

    def list_by_author(self, author):
        search_results = []
        for book in self.data_repository.book_list:
            if book.author == author:
                search_results.append(book)
        return search_results

    def list_by_isbn(self, isbn):
        search_results = []
        for book in self.data_repository.book_list:
            if book.isbn == isbn:
                search_results.append(book)
        return search_results
