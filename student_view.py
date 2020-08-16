from operations import StudentOperations
# TODO zrobić by StudentView nie printował list


class StudentView:

    def __init__(self, student_operations: StudentOperations):
        self.student_operations = student_operations
        self.edit_view_component = StudentEditViewComponent(student_operations)
        self.search_view_component = StudentSearchViewComponent(student_operations)

    def edit(self):
        self.edit_view_component.edit()

    def search(self):
        self.search_view_component.search()

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


class StudentSearchViewComponent:
    def __init__(self, student_operations):
        self.student_operations = student_operations

    def search(self):
        data = input("Please type student's full name, surname, ID or pesel number: ")
        search_result = self.student_operations.search(data)
        if len(search_result) > 1:
            index = self.pick_index_from_list(search_result)
            student = search_result[index - 1]
            return student
        else:
            print('There is no such student in the library.')
            pass

    @staticmethod
    def pick_index_from_list(search_result):
        print(search_result)
        index = int(input('Please pick student from the list (enter number): '))
        if len(search_result) < index:
            pass
        return int(index)


class StudentEditViewComponent:
    def __init__(self, student_operations):
        self.student_operations = student_operations

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

    def edit_name(self, student):
        new_name = input('Enter new first name: ')
        self.student_operations.set_name(new_name, student)
        print('Name successfully changed to', new_name, '!')
        pass

    def edit_surname(self, student):
        new_surname = input('Enter new surname: ')
        self.student_operations(new_surname, student)
        print('Surname successfully changed to', new_surname, '!')
        pass

    def edit_pesel(self, student):
        new_pesel = str(input('Enter new PESEL: '))
        self.student_operations(new_pesel, student)
        print('PESEL successfully changed to:', new_pesel)
        pass
