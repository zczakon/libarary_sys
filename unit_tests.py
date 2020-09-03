import unittest

from pony.orm import db_session

from data_source import SqlDataRepository
from domain_objects import Student, Book
from operations import StudentOperations, BookOperations, BookLendingOperations
import datetime

with db_session:
    student = Student(name='Zuzia', surname='Czakon', pesel='456')
    student2 = Student(name='Michał', surname='Jakiś', pesel='123')
    book = Book(isbn='1010101010333', title='Ulysses', author='James Joyce')
    student.create()
    student2.create()
    data_repository = SqlDataRepository()
    student_operations = StudentOperations(data_repository)
    book_operations = BookOperations(data_repository)
    book_lending_operations = BookLendingOperations(data_repository)


    class TestDomainObjects(unittest.TestCase):
        def test_is_overdue(self):
            pass


    class TestStudentOperations(unittest.TestCase):
        def test_search_by_pesel(self):
            self.assertEqual(student_operations.search_by_pesel('456'), [student])
            self.assertEqual(student_operations.search_by_pesel('123'), [student2])

        def test_search_by_name(self):
            self.assertEqual(student_operations.search_by_name('Zuzia'), [student])
            self.assertEqual(student_operations.search_by_name('Cz'), [])

        def test_search_by_surname(self):
            self.assertEqual(student_operations.search_by_surname('Czakon'), [student])
            self.assertEqual(student_operations.search_by_surname('Cz'), [])

        def test_search_by_fullname(self):
            self.assertEqual(student_operations.search_by_fullname('Zuzia Czakon'), [student])
            self.assertEqual(student_operations.search_by_fullname('Cz'), [])

        def test_search(self):
            self.assertEqual(student_operations.search('123'), [student2])
            self.assertEqual(student_operations.search(123), [])
            self.assertEqual(student_operations.search('1234'), [])
            self.assertEqual(student_operations.search('Zuzia'), [student])
            self.assertEqual(student_operations.search('Cz'), [])
            self.assertEqual(student_operations.search('Czakon'), [student])
            self.assertEqual(student_operations.search('Cz'), [])
            self.assertEqual(student_operations.search('Zuzia Czakon'), [student])
            self.assertEqual(student_operations.search('Cz'), [])
            self.assertEqual(student_operations.search('Cz'), [])


    class TestBookOperations(unittest.TestCase):

        def test_list_available(self):
            student_id = student.id
            book_id = book.id
            self.assertEqual(book_operations.list_available(), data_repository.book_list())
            book_operations.lend_book(student_id, book_id)
            self.assertEqual(book_operations.list_available(), [])
            pass

        def test_list_pending(self):
            student_id = student.id
            book_id = book.id
            book_operations.lend_book(student_id, book_id)
            self.assertEqual(book_operations.list_pending(), [book])
            book_operations.return_book(book_id)
            self.assertEqual(book_operations.list_pending(), [])


    class TestBookLendingOperations(unittest.TestCase):

        def test_list_overdue(self):
            book_lending = book_operations.lend_book(student.id, book.id)
            self.assertEqual(book_lending_operations.list_overdue(), [])
            book_lending.set(creation_date=datetime.date(2010, 12, 21))
            book_lending.set(max_return_date=book_lending.creation_date + datetime.timedelta(days=30))
            self.assertEqual(book_lending_operations.list_overdue(), [book_lending])

        def test_search_by_student(self):
            book_lending = book_operations.lend_book(student.id, book.id)
            self.assertEqual(book_lending_operations.search_by_student(student), [book_lending])
