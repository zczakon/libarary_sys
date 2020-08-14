from operations import BookOperations, StudentOperations


class BookView:
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


class BookEditView(BookView):
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
        if book is None:
            print('No book with matching data!')
            pass

        self.display_edit_menu()
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
        new_isbn = int(input('Enter new ISBN number: '))
        book.set_isbn(new_isbn)
        print('ISBN number successfully changed to', new_isbn)
        pass
