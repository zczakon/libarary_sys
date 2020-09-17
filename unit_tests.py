import unittest

from data_source import SqlDataRepository
from domain_objects import Student, Book
from operations import StudentOperations, BookOperations, BookLendingOperations
import datetime


class TestStudentSearchOperations(unittest.TestCase):
    student = Student('Zuzia', 'Czakon', 1231231231)
    student2 = Student('Michał', 'Jakiś', 1231231231)
    data_repository = SqlDataRepository([student, student2], [])
    student_operations = StudentOperations(data_repository)

    def test_search_by_pesel(self):
        self.assertEqual(self.student_operations.search_by_pesel(1231231231), [self.student, self.student2])
        self.assertEqual(self.student_operations.search_by_pesel(123), [])

    def test_search_by_name(self):
        self.assertEqual(self.student_operations.search_by_name('Zuzia'), [self.student])
        self.assertEqual(self.student_operations.search_by_name('Cz'), [])

    def test_search_by_surname(self):
        self.assertEqual(self.student_operations.search_by_surname('Czakon'), [self.student])
        self.assertEqual(self.student_operations.search_by_surname('Cz'), [])

    def test_search_by_fullname(self):
        self.assertEqual(self.student_operations.search_by_fullname('Zuzia Czakon'), [self.student])
        self.assertEqual(self.student_operations.search_by_fullname('Cz'), [])

    def test_search_by_id(self):
        self.assertEqual(self.student_operations.search_by_id(id(self.student)), [self.student])
        self.assertEqual(self.student_operations.search_by_id('Cz'), [])

    def test_search(self):
        self.assertEqual(self.student_operations.search(1231231231), [self.student, self.student2])
        self.assertEqual(self.student_operations.search(123), [])
        self.assertEqual(self.student_operations.search('Zuzia'), [self.student])
        self.assertEqual(self.student_operations.search('Cz'), [])
        self.assertEqual(self.student_operations.search('Czakon'), [self.student])
        self.assertEqual(self.student_operations.search('Cz'), [])
        self.assertEqual(self.student_operations.search('Zuzia Czakon'), [self.student])
        self.assertEqual(self.student_operations.search('Cz'), [])
        self.assertEqual(self.student_operations.search(id(self.student)), [self.student])
        self.assertEqual(self.student_operations.search('Cz'), [])


class TestBookOperations(unittest.TestCase):
    book = Book(1010101010333, 'Ulysses', 'James Joyce')
    student = Student('Zuzia', 'Czakon', 123)
    data_repository = SqlDataRepository([student], [book])
    book_operations = BookOperations(data_repository)
    student_operations = StudentOperations(data_repository)

    def test_search_by_id(self):
        self.assertEqual(self.book_operations.search_by_id(id(self.book)), [self.book])

    def test_list_available(self):
        self.assertEqual(self.book_operations.list_available(), self.data_repository.get_book_list())
        self.book_operations.lend_book(self.student, self.book)
        self.assertEqual(self.book_operations.list_available(), [])
        pass

    def test_list_pending(self):
        self.book_operations.lend_book(self.student, self.book)
        self.assertEqual(self.book_operations.list_pending(), [self.book])
        self.book_operations.return_book(self.book)
        self.assertEqual(self.book_operations.list_pending(), [])


class TestBookLendingOperations(unittest.TestCase):
    book = Book(1010101010333, 'Ulysses', 'James Joyce')
    student = Student('Zuzia', 'Czakon', 123)
    data_repository = SqlDataRepository([student], [book])
    book_operations = BookOperations(data_repository)
    student_operations = StudentOperations(data_repository)
    book_lending_operations = BookLendingOperations(data_repository)

    def test_list_overdue(self):
        book_lending = self.book_operations.lend_book(self.student, self.book)
        self.assertEqual(self.book_lending_operations.list_overdue(), [])
        book_lending.set_creation_date(datetime.date(2010, 12, 21))
        book_lending.max_return_date = book_lending.get_creation_date() + datetime.timedelta(days=30)
        self.assertEqual(self.book_lending_operations.list_overdue(), [book_lending])

    def test_is_overdue(self):
        book_lending = self.book_operations.lend_book(self.student, self.book)
        book_lending.set_creation_date(datetime.date.today() - datetime.timedelta(days=40))
        book_lending.max_return_date = book_lending.get_creation_date() + datetime.timedelta(days=30)
        print(book_lending.creation_date)
        print(book_lending.max_return_date)
        self.assertTrue(datetime.date.today() > book_lending.get_max_return_date())

    def test_search_by_student(self):  # lendings_per_student ok
        book_lending = self.book_operations.lend_book(self.student, self.book)
        self.assertEqual(self.book_lending_operations.search_by_student(self.student), [book_lending])
