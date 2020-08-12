from operations import StudentOperations, BookOperations


class StudentInterface:

    def __init__(self, student_operations: StudentOperations):
        self.student_operations = student_operations

    def add(self):
        name = input('Type name of student you want to add: ')
        surname = input('Type surname of student you want to add: ')
        pesel: int = int(input('Type pesel of student you want to add: '))
        student = self.student_operations.add(name, pesel, surname)
        print('Student', student.name, student.surname, 'successfully added!')
        pass

    def list(self):
        student_list = self.student_operations.list()
        if student_list:
            print('Current list of students in the library:')
            print(student_list)
        else:
            print('There are no students in the library.')

    def delete(self):
        self.list()
        student_list = self.student_operations.list()
        if not student_list:
            pass

        to_delete = input('Which student do you want to delete? ')
        student = self.student_operations.delete(to_delete)
        if student:
            print('Student ', student, ' was successfully deleted.')
        else:
            print('No such student.')
        pass


class BookInterface:
    def __init__(self, book_operations: BookOperations, student_operations: StudentOperations):
        self.book_operations = book_operations
        self.student_operations = student_operations

    def add(self):
        isbn = int(input('Type ISBN number of the book you want to add: '))
        title = input('Type title of the book you want to add: ')
        author = input('Type author of the book you want to add: ')
        self.book_operations.add(author, isbn, title)
        pass

    def list(self):
        book_list = self.book_operations.list()
        if book_list:
            print('Books in the library:')
            print(book_list)
        else:
            print('There are no books in the library.')

    def list_available(self):
        available_book_list = self.book_operations.list_available()
        if available_book_list:
            print('Books available to lend:')
            print(available_book_list)
        else:
            print('There are no available books in the library.')

    def delete(self):
        self.list()
        book_list = self.book_operations.list()
        if not book_list:
            pass

        to_delete: str = input('Which book do you want to delete? ')
        book = self.book_operations.delete(to_delete)

        if book:
            print('Book', book, 'was successfully deleted.')
        else:
            print('No such book.')
        pass

    def lend(self):
        student_name_surname = input('Please insert students name and surname. ')
        student = self.student_operations.search(student_name_surname)

        print('List of books available in the library: ')
        self.list_available()
        available_book_list = self.book_operations.list_available()

        to_lend = input('Which book do you want to lend? ')
        if to_lend not in available_book_list:
            pass

        book = self.book_operations.search(to_lend)
        student.lend_book(book)
        pass

    def return_book(self):
        student_name_surname = input('Please insert students name and surname. ')
        student = self.student_operations.search(student_name_surname)
        to_return = input('Which book do you want to return? ')
        book = self.book_operations.search(to_return)
        student.return_book(book)
        print(book.title, 'was successfully returned')
        pass
