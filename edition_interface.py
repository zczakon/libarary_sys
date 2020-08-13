from interface import StudentInterface, BookInterface


class EditStudent(StudentInterface):
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
        student = self.student_operations.student_search.search(to_edit)
        if student is None:
            print('No student with matching data!')
            pass

        self.display_edit_menu()
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


class EditBook(BookInterface):
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
        book = self.book_operations.book_search.search(to_edit)
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
