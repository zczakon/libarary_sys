

class SqlDataRepository:
    def student_list(self):
        pass

    def book_list(self):
        pass

    def lending_list(self):
        pass

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
        available = [book for book in self.book_list if self.is_lent(book) is False]
        return available

    def overdue_book_list(self):
        overdue_lendings = [lending for lending in self.lending_history if lending.is_overdue()]
        return overdue_lendings

    def is_lent(self, book):
        for lending in self.lending_history:
            if lending.book == book and lending.return_date is None:
                return True
        return False
