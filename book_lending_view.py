# TODO zrobić by BookLendingView nie printował list


class BookLendingView:
    def __init__(self, book_lending_operations, book_lending_search_view_component, book_search_view):
        self.book_lending_operations = book_lending_operations
        self.book_lending_search_view_component = book_lending_search_view_component
        self.book_search_view = book_search_view

    def search(self):
        self.book_lending_search_view_component.search()

    @staticmethod
    def display_check_date_time_menu():
        menu = {'1': 'Check creation date', '2': 'Check return date', '3': 'Check remaining days',
                '4': 'Check rental time', '5': 'See overdue lendings'}
        options = menu.keys()
        print('Options: ')
        for entry in options:
            print(entry, menu[entry])
        pass

    def display_lending_history(self) -> list:
        flat_lending_history = self.book_lending_operations.flatten_lending_history()
        print(flat_lending_history)
        return flat_lending_history

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
            self.see_overdue()
        else:
            print('Wrong option selected')
        pass

    def check_rental_time(self):
        lending_history: list = self.display_lending_history()
        index = self.ask_for_book_lending_index()
        self.book_lending_operations.check_rental_time(lending_history[index - 1])
        pass

    def check_remaining_days(self):
        lending_history: list = self.display_lending_history()
        index = self.ask_for_book_lending_index()
        remaining_days = lending_history[index - 1].remaining_days()
        if remaining_days:
            return remaining_days
        print('Book has already been returned! ')
        pass

    def check_return_date(self):
        lending_history: list = self.display_lending_history()
        index = self.ask_for_book_lending_index()
        return_date = lending_history[index - 1].get_return_date()
        if return_date is None:
            print('Book has not yet been returned!')
            pass
        return return_date

    def check_creation_date(self):
        lending_history: list = self.display_lending_history()
        index = self.ask_for_book_lending_index()
        creation_date = lending_history[index - 1].get_creation_date()
        return creation_date

    def see_overdue(self):
        """
        :return: list of all overdue lendings
        """
        print('All overdue lendings in the library: ')
        self.book_lending_operations.see_overdue()
        pass


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
            self.search_by_student()
        if selection is '2':
            self.search_by_book()
        pass

    def search_by_student(self):
        """
        :return: list of lendings per student
        """
        student = self.student_search_view.search()
        if student is None:
            pass
        search_results = self.book_lending_operations.search_by_student(student)
        return search_results

    def search_by_book(self):
        """
        :return: list of lendings per book
        """
        book = self.book_search_view.search()
        if book is None:
            pass
        search_results = self.book_lending_operations.search_by_book(book)
        return search_results
