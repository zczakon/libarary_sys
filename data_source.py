
class Lists:

    def __init__(self, student_list, book_list, lending_history):
        self.student_list = student_list
        self.book_list = book_list
        self.lending_history = lending_history  # list of lists of student.lending's

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

    def lendings_per_student(self, student):
        for i in range(len(self.lending_history)):
            if self.lending_history[i] == student.lendings:  # student.lendings -> self.lendings should be created
                # instead of books_lent
                return student.lendings

    def lendings_per_book(self, book):
        lendings_of_book = []
        for i in range(len(self.lending_history)):
            for lending in self.lending_history[i]:  # is a list of book lendings
                if lending.book == book:
                    lendings_of_book.append(lending)
        pass
