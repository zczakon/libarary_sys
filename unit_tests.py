import unittest

from data_source import DataRepository
from domain_objects import Student, Book
from operations import StudentOperations, BookOperations


class TestStudentSearchOperations(unittest.TestCase):
    student = Student('Zuzia', 'Czakon', 1231231231)
    student2 = Student('Michał', 'Jakiś', 1231231231)
    data_repository = DataRepository([student, student2], [])
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
    data_repository = DataRepository([], [book])
    book_operations = BookOperations(data_repository)

    def test_search_by_id(self):
        self.assertEqual(self.book_operations.search_by_id(id(self.book)), [self.book])
