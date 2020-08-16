from operations import BookOperations
from student_view import StudentSearchViewComponent
# TODO zrobić by BookView nie printował list


class BookView:
    book_operations: BookOperations

    def __init__(self, book_operations: BookOperations, student_search_view: StudentSearchViewComponent):
        self.book_operations = book_operations
        self.edit_view_component = BookEditViewComponent(book_operations)
        self.search_view_component = BookSearchViewComponent(book_operations)
        self.student_search_view = student_search_view

    def edit(self):
        self.edit_view_component.edit()

    def search(self):
        self.search_view_component.search()

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
        student = self.student_search_view.search()

        print('List of books available in the library: ')
        self.list_available()
        to_lend = input('Which book do you want to lend? ')
        is_available = self.book_operations.is_available(to_lend)
        if is_available:
            book = self.book_operations.search(to_lend)
            student.lend_book(book)
        pass

    @staticmethod
    def is_available(available_book_list, to_lend):
        if to_lend not in available_book_list:
            pass

    def return_book(self):
        student = self.student_search_view.search()

        to_return = input('Which book do you want to return? ')
        book = self.book_operations.search(to_return)

        student.return_book(book)
        print('"' + book.title + '"', 'was successfully returned')
        pass


class BookSearchViewComponent:
    def __init__(self, book_operations):
        self.book_operations = book_operations

    def search(self):
        data = input("Please type book's title, author, ID or ISBN number: ")
        search_result = self.book_operations.search(data)
        if search_result:
            print(search_result)
            return search_result
        else:
            print('There is no such book in the library.')
            pass


class BookEditViewComponent:
    def __init__(self, book_operations):
        self.book_operations = book_operations

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

    def edit_title(self, book):
        new_title = input('Enter new title: ')
        self.book_operations.set_title(book, new_title)
        print('Title successfully changed to', '"' + new_title + '"!')
        pass

    def edit_author(self, book):
        new_author = input('Enter new author: ')
        self.book_operations.set_author(book, new_author)
        print('Author successfully changed to', new_author, '!')
        pass

    def edit_isbn(self, book):
        new_isbn = int(input('Enter new ISBN number: '))
        self.book_operations.set_isbn(book, new_isbn)
        print('ISBN number successfully changed to', new_isbn)
        pass
