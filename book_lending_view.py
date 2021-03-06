from book_view import BookSearchViewComponent
from student_view import StudentSearchViewComponent


class BookLendingView:
    def __init__(self, book_lending_operations, book_search_view: BookSearchViewComponent,
                 student_search_view: StudentSearchViewComponent):
        self.book_lending_operations = book_lending_operations
        self.book_lending_search_view_component = BookLendingSearchViewComponent(
            student_search_view, book_search_view, book_lending_operations)

    def search(self):
        book_lending = self.book_lending_search_view_component.search()
        return book_lending

    @staticmethod
    def display_check_date_time_menu():
        menu = {'1': 'Check creation date', '2': 'Check return date', '3': 'Check remaining days',
                '4': 'Check rental time', '5': 'See overdue lendings'}
        options = menu.keys()
        print('Options: ')
        for entry in options:
            print(entry, menu[entry])
        pass

    @staticmethod
    def ask_for_book_lending_index():
        num_in_list = int(input('Choose book lending from the list (enter number of item in the list): '))
        return num_in_list

    def check_date_time(self):
        self.display_check_date_time_menu()
        selection = input()
        if selection is '1':
            self.check_creation_date()
        elif selection is '2':
            self.check_return_date()
        elif selection is '3':
            self.check_remaining_days()
        elif selection is '4':
            self.check_rental_time()
        elif selection is '5':
            self.list_overdue()
        else:
            print('Wrong selection! ')
        pass

    def check_rental_time(self):
        book_lending = self.search()
        rental_time = self.book_lending_operations.check_rental_time(book_lending)
        print('Rental time:', rental_time)
        return rental_time

    def check_remaining_days(self):
        book_lending = self.search()
        remaining_days = book_lending.remaining_days()
        if remaining_days:
            print('Remaining days:', remaining_days)
            return remaining_days
        print('Book has already been returned! ')
        pass

    def check_return_date(self):
        book_lending = self.search()
        return_date = book_lending.get_return_date()
        if return_date is None:
            print('Book has not yet been returned!')
            pass
        print('Return date:', return_date)
        return return_date

    def check_creation_date(self):
        book_lending = self.search()
        creation_date = book_lending.get_creation_date()
        print('Creation date:', creation_date)
        return creation_date

    def list_overdue(self):
        """
        :return: list of all overdue lendings
        """
        overdue = self.book_lending_operations.list_overdue()
        if overdue:
            print('All overdue lendings in the library:', overdue)
        else:
            print('No overdue lendings.')
        return overdue


class BookLendingSearchViewComponent:
    def __init__(self, student_search_view, book_search_view, book_lending_operations):
        self.book_lending_operations = book_lending_operations
        self.student_search_view = student_search_view
        self.book_search_view = book_search_view

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
            return self.search_by_student()
        if selection is '2':
            return self.search_lending_by_book()
        else:
            print('Wrong selection! ')

    def search_by_student(self):
        student = self.student_search_view.search_single()
        if student is None:
            pass

        search_result = self.book_lending_operations.search_by_student(student)  # evals to []?
        lending = self.pick_single(search_result)
        print('Search result:', search_result)
        return lending

    def search_lending_by_book(self):
        book = self.book_search_view.search_single()
        if book is None:
            pass

        search_result = self.book_lending_operations.search_by_book(book)
        lending = self.pick_single(search_result)
        print('Search result:', search_result)
        return lending

    @staticmethod
    def pick_index_from_list(search_result):
        print(search_result)
        index = int(input('Please pick book lending from the list (enter number): '))
        if len(search_result) < index:
            pass
        return int(index)

    def pick_single(self, search_result):
        if len(search_result) > 1:
            index = self.pick_index_from_list(search_result)
            book = search_result[index - 1]
            print('Found book lending:', book)
            return book
        elif len(search_result) == 1:
            print('Found book lending:', search_result[0])
            return search_result[0]
        else:
            print('There are no such lendings.')
