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
            print('Student ', student.name, student.surname, ' was successfully deleted.')
        else:
            print('No such student.')
        pass

    def search(self):
        data = input("Please type student's full name, surname, ID or pesel number: ")
        search_result = self.student_operations.search(data)
        if search_result:
            print(search_result)
        else:
            print('There is no such student in the library.')

    @staticmethod
    def display_edit_menu():
        menu = {'1': 'Edit Name', '2': 'Edit Surname', '3': 'Edit PESEL'}
        options = menu.keys()
        print('Options: ')
        for entry in options:
            print(entry, menu[entry])
        pass

    def edit(self):
        to_edit = input('Which book do you want to edit?')
        student = self.student_operations.search(to_edit)
        selection = input()
        if selection == '1':
            self.edit_name(student)
        elif selection == '2':
            self.edit_surname(student)
        elif selection == '3':
            self.edit_pesel(student)
        else:
            print('Wrong selection!')

    @staticmethod
    def edit_name(student):
        new_name = input('Enter new first name: ')
        student.set_name(new_name)
        print('Name successfully changed to', new_name, '!')
        pass

    @staticmethod
    def edit_surname(student):
        new_surname = input('Enter new surname: ')
        student.set_surname(new_surname)
        print('Surname successfully changed to', new_surname, '!')
        pass

    @staticmethod
    def edit_pesel(student):
        new_pesel = str(input('Enter new PESEL: '))
        student.set_pesel(new_pesel)
        print('PESEL successfully changed to:', new_pesel)
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
        else:
            print('There is no such book in the library.')
        pass

    @staticmethod
    def display_edit_menu():
        menu = {'1': 'Edit Title', '2': 'Edit Author', '3': 'Edit ISBN'}
        options = menu.keys()
        print('Options: ')
        for entry in options:
            print(entry, menu[entry])
        pass

    def edit(self):
        to_edit = input('Which book do you want to edit?')
        book = self.book_operations.search(to_edit)
        selection = input()
        if selection == '1':
            self.edit_title(book)
        elif selection == '2':
            self.edit_author(book)
        elif selection == '3':
            self.edit_isbn(book)
        else:
            print('Wrong selection!')

    @staticmethod
    def edit_title(book):
        new_title = input('Enter new title: ')
        book.set_title(new_title)
        print('Title successfully changed to', '"' + new_title + '"!')
        pass

    @staticmethod
    def edit_author(book):
        new_author = input('Enter new author: ')
        book.set_author(new_author)
        print('Author successfully changed to', new_author, '!')
        pass

    @staticmethod
    def edit_isbn(book):
        new_isbn = input('Enter new ISBN number: ')
        book.set_isbn(new_isbn)
        print('ISBN number successfully changed to', new_isbn)
        pass
