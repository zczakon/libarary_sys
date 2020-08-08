class Lists:
    def __init__(self, student_list, book_list):
        self.student_list = student_list
        self.book_list = book_list

    def add_student(self, student):
        self.student_list.append(student)
        pass

    def del_student(self, student):
        self.student_list.remove(student)
        pass

    def add_book(self, book):
        self.book_list.append(book)
        pass

    def del_book(self, book):
        self.book_list.remove(book)
        pass

    def get_student_list(self):
        return self.student_list

    def get_book_list(self):
        return self.book_list
