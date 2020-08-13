from typing import Dict

from data_source import DataRepository
from edition_interface import EditBook, EditStudent
from interface import StudentInterface, BookInterface, BookLendingInterface
from operations import StudentOperations, BookOperations, BookLendingOperations


def main():
    data_repository: DataRepository = DataRepository([], [])

    student_operations = StudentOperations(data_repository)
    student_interface = StudentInterface(student_operations)
    book_operations = BookOperations(data_repository)
    book_lending_operations = BookLendingOperations(data_repository)
    book_interface = BookInterface(book_operations, student_operations)
    book_lending_interface = BookLendingInterface(book_lending_operations, student_interface, book_interface)

    edit_student = EditStudent(student_operations)
    edit_book = EditBook(book_operations, student_operations)

    print('Hello and welcome to The Library. Choose your action from the menu: ')
    menu: Dict[str, str] = {'1': 'Add Student', '2': 'Delete Student', '3': 'Add Book', '4': 'Delete Book',
                            '5': 'Lend Book', '6': 'Return Book', '7': 'Search Student', '8': 'Search Book',
                            '9': 'Edit Student', '10': 'Edit Book', '11': 'Search Book Lending',
                            '12': 'See Overdue Book Lendings', '13': 'Exit'}

    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection = input("Please Select: ")

        if selection == '1':
            student_interface.add()
        elif selection == '2':
            student_interface.delete()
        elif selection == '3':
            book_interface.add()
        elif selection == '4':
            book_interface.delete()
        elif selection == '5':
            book_interface.lend()
        elif selection == '6':
            book_interface.return_book()
        elif selection == '7':
            student_interface.search()
        elif selection == '8':
            book_interface.search()
        elif selection == '9':
            edit_student.edit()
        elif selection == '10':
            edit_book.edit()
        elif selection == '11':
            book_lending_interface.search()
        elif selection == '12':
            book_lending_interface.see_overdue()
        elif selection == '13':
            break
        else:
            print("Unknown Option Selected!")
        pass


main()
