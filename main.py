from data_source import DataRepository
from interface import StudentInterface, BookInterface
from operations import StudentOperations, BookOperations


def main():

    data_repository = DataRepository([], [])
    student_operations = StudentOperations(data_repository)
    student_interface = StudentInterface(student_operations)
    book_operations = BookOperations(data_repository)
    book_interface = BookInterface(book_operations, student_operations)

    print('Hello and welcome to The Library. Choose your action from the menu: ')
    menu = {'1': 'Add Student', '2': 'Delete Student', '3': 'Add Book', '4': 'Delete Book',
            '5': 'Lend Book', '6': 'Return Book', '7': 'Exit'}

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
            break
        else:
            print("Unknown Option Selected!")
        pass


main()
