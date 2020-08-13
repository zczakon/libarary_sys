from operations import StudentOperations, BookOperations


class StudentInterface:

    def __init__(self, student_operations: StudentOperations):
        self.student_operations = student_operations

    def add(self):
        name = input('Type name of student you want to add: ')
        surname = input('Type surname of student you want to add: ')
        pesel = int(input('Type pesel of student you want to add: '))
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
            print('Student ', student.name, student.surname, ' was successfully deleted.')
        else:
            print('No such student.')
        pass

    def search(self):
        data = input("Please type student's full name, surname, ID or pesel number: ")
        search_result = self.student_operations.search(data)
        if search_result:
            print(search_result)
            return search_result
        else:
            print('There is no such student in the library.')
            pass


class BookInterface:
    book_operations: BookOperations

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
            print('Book', '"' + book.title + '"', 'was successfully deleted.')
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
        student_fullname = input('Please insert students name and surname. ')
        student = self.student_operations.search(student_fullname)

        to_return = input('Which book do you want to return? ')
        book = self.book_operations.search(to_return)

        student.return_book(book)
        print('"' + book.title + '"', 'was successfully returned')
        pass

    def search(self):
        data = input("Please type book's title, author, ID or ISBN number: ")
        search_result = self.book_operations.search(data)
        if search_result:
            print(search_result)
            return search_result
        else:
            print('There is no such book in the library.')
            pass


class BookLendingInterface:
    def __init__(self, book_lending_operations, student_interface, book_interface):
        self.book_lending_operations = book_lending_operations
        self.student_interface = student_interface
        self.book_interface = book_interface

    @staticmethod
    def display_search_menu():
        menu = {'1': 'Search by Student', '2': 'Search by Book'}
        options = menu.keys()
        print('Options: ')
        for entry in options:
            print(entry, menu[entry])
        pass

    def search(self):
        self.display_search_menu()
        selection = input()
        if selection is '1':
            self.search_by_student()
        if selection is '2':
            self.search_by_book()
        pass

    def search_by_student(self):
        student = self.student_interface.search()
        if student is None:
            pass
        search_results = self.book_lending_operations.search_by_student(student)
        return search_results

    def search_by_book(self):
        book = self.book_interface.search()
        if book is None:
            pass
        search_results = self.book_lending_operations.search_by_book(book)
        return search_results

    def see_overdue(self):
        """
        :return: list of all overdue lendings
        """
        print('All overdue lendings in the library: ')
        self.book_lending_operations.see_overdue()
        pass
