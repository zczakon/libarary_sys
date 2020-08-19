from library_components import Student, Book


class StudentOperations:
    def __init__(self, data_repository):
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
        result = self.search_by_title(data) + self.search_by_author(data) + self.search_by_isbn(data) + \
                 self.search_by_id
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

    def list_pending(self):
        return self.data_repository.pending_book_list()


class BookLendingOperations:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def search(self, data):
        result = self.search_by_student(data) + self.search_by_book(data)
        return result

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
