import unittest

from data_source import SqlDataRepository
from domain_objects import Student, Book, BookLending
import db
from operations import StudentOperations
from sqlalchemy.orm import sessionmaker

data_repository = SqlDataRepository()


class TestQuery(unittest.TestCase):
    engine = db.create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        db.Base.metadata.create_all(self.engine)

        self.student1 = Student(name='Zuzia', surname='Czakon', pesel='1231231231').create()
        self.student2 = Student(name='Michał', surname='Jakiś', pesel='1231231231').create()
        self.book = Book(isbn='1010101010333', title='Ulysses', author='James Joyce')
        self.book_lending = BookLending(student=self.student1, book=self.book).create()

        self.session.add_all([self.student1, self.student2, self.book, self.book_lending])
        self.session.commit()

    def tearDown(self):
        db.Base.metadata.drop_all(self.engine)
        self.session.rollback()

    def test_query_student(self):
        expected = [self.student1, self.student2]
        result = self.session.query(Student).all()
        self.assertEqual(result, expected)

    def test_query_book(self):
        expected = [self.book]
        result = self.session.query(Book).all()
        self.assertEqual(result, expected)

    def test_query_book_lending(self):
        expected = [self.book_lending]
        result = self.session.query(BookLending).all()
        self.assertEqual(result, expected)


class TestStudentOperations(unittest.TestCase):
    engine = db.create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        db.Base.metadata.create_all(self.engine)

        self.student1 = Student(name='Zuzia', surname='Czakon', pesel='1231231231').create()
        self.student2 = Student(name='Michał', surname='Jakiś', pesel='1231231231').create()
        self.session.add_all([self.student1, self.student2])
        self.session.commit()

        self.student_operations = StudentOperations(data_repository)

    def tearDown(self):
        db.Base.metadata.drop_all(self.engine)
        self.session.rollback()

    def test_add(self):
        student3 = self.student_operations.add('Zuzia', 'Czakon', '30364')
        self.session.add(student3)
        self.session.commit()

        result = self.session.query(Student).all()
        print('result:', result)

        expected = [self.student1, self.student2, student3]
        self.assertEqual(result, expected)

    def test_list(self):
        student = self.student_operations.add('Zuzia', 'Czakon', '30364')
        student2 = self.student_operations.add('Michał', 'Jakiś', '123')
        self.session.add_all([student, student2])
        self.session.commit()
        expected = [student, student2]
        result = self.student_operations.list()
        self.assertEqual(result, expected)
