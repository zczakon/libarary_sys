from typing import Dict

from data_source import DataRepository
from book_view import BookView, BookSearchViewComponent
from student_view import StudentView, StudentSearchViewComponent
from book_lending_view import BookLendingView
from operations import StudentOperations, BookOperations, BookLendingOperations


def main():
    data_repository: DataRepository = DataRepository([], [])

    student_operations = StudentOperations(data_repository)
    book_operations = BookOperations(data_repository)
    book_lending_operations = BookLendingOperations(data_repository)

    student_view = StudentView(student_operations)
    student_search_view = StudentSearchViewComponent(student_operations)

    book_search_view = BookSearchViewComponent(book_operations)
    book_view = BookView(book_operations, student_search_view)

    book_lending_view = BookLendingView(book_lending_operations, book_search_view, student_search_view)

    print('Hello and welcome to The Library. Choose your action from the menu: ')
    menu: Dict[str, str] = {'1': 'Add Student', '2': 'Delete Student', '3': 'Add Book', '4': 'Delete Book',
                            '5': 'Lend Book', '6': 'Return Book', '7': 'Search Student', '8': 'Search Book',
                            '9': 'Edit Student', '10': 'Edit Book', '11': 'Search Book Lending',
                            '12': 'See Overdue Book Lendings', '13': 'Check date/time for Book Lending', '14': 'Exit'}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")

        if selection == '1':
            student_view.add()
        elif selection == '2':
            student_view.delete()
        elif selection == '3':
            book_view.add()
        elif selection == '4':
            book_view.delete()
        elif selection == '5':
            book_view.lend()
        elif selection == '6':
            book_view.return_book()
        elif selection == '7':
            student_view.search()
        elif selection == '8':
            book_view.search()
        elif selection == '9':
            student_view.edit()
        elif selection == '10':
            book_view.edit()
        elif selection == '11':
            book_lending_view.search()
        elif selection == '12':
            book_lending_view.list_overdue()
        elif selection == '13':
            book_lending_view.check_date_time()
        elif selection == '14':
            break
        else:
            print("Unknown Option Selected!")
        pass


main()
