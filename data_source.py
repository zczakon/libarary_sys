class DataRepository:

    def __init__(self, student_list, book_list):
        self.student_list = student_list
        self.book_list = book_list
        self.lending_history = []

    def add_student(self, student):
        self.student_list.append(student)
        # print('Current student list:', self.student_list)  # remove
        pass

    def delete_student(self, student):
        self.student_list.remove(student)
        pass

    def add_book(self, book):
        self.book_list.append(book)
        pass

    def delete_book(self, book):
        self.book_list.remove(book)
        pass

    def get_student_list(self):
        return self.student_list

    def get_book_list(self):
        return self.book_list

    def get_available_book_list(self):
        return self.available_book_list()

    def get_pending_book_list(self):
        return self.pending_book_list()

    def get_lending_history(self):
        return self.lending_history

    def lendings_per_student(self, student):
        student_lendings = [lending for lending in self.lending_history if lending.student == student]
        return student_lendings

    def lendings_per_book(self, book):
        books_lendings = [lending for lending in self.lending_history if lending.book == book]
        return books_lendings

    def pending_book_list(self):
        pending = [lending.book for lending in self.lending_history if lending.return_date is None]
        return pending

    def available_book_list(self):
        available = [book for book in self.book_list if book not in self.pending_book_list]
        return available

    def overdue_book_list(self):
        overdue_lendings = [lending for lending in self.lending_history if lending.is_overdue()]
        return overdue_lendings
