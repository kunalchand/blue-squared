import unittest
import sys
import os

from repository import DatabaseRepository


# Unit Test Cases
class TestDatabaseRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db_url = "sqlite:///test_database.db"  # SQLite DB for testing
        from repository import create_engine,sessionmaker
        cls.engine = create_engine(db_url)
        cls.session = sessionmaker(bind=cls.engine)()

        # Create tables in the test database
        from Model.models import Base  # Assuming Base is the declarative base for models
        Base.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        # Drop tables after tests
        from Model.models import Base
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        """Setup test data before each test."""
        from Model.models import Person,Person2
        db_repo = DatabaseRepository()
        db_repo.session.add(Person(id=1, name="John Doe"))
        db_repo.session.add(Person2(id=1, name="Liam Turner"))
        db_repo.session.commit()

    def tearDown(self):
        """Clear the session after each test."""
        from Model.models import Person,Person2
        self.session.query(Person).delete()
        self.session.query(Person2).delete()

        self.session.commit()

    def test_get_record_valid_person(self):
        db_repo = DatabaseRepository()
        person_record = db_repo.get_record_from_table1(1)
        self.assertIsNotNone(person_record)
        self.assertEqual(person_record.id, 1)

    def test_get_record_valid_person2(self):
        db_repo = DatabaseRepository()
        person2_record = db_repo.get_record_from_table2(1)
        self.assertIsNotNone(person2_record)
        self.assertEqual(person2_record.id, 1)

    def test_get_record_non_existing_person(self):
        db_repo = DatabaseRepository()
        person_record = db_repo.get_record_from_table1(99999)  # Assuming this ID does not exist
        self.assertIsNone(person_record)

    def test_get_record_invalid_id_type(self):
        db_repo = DatabaseRepository()
        with self.assertRaises(ValueError):  # Example: expect ValueError when passing string
            db_repo.get_record_from_table1("abc")

    def test_get_record_invalid_table(self):
        db_repo = DatabaseRepository()
        with self.assertRaises(AttributeError):  # Expecting error when passing None
            db_repo.get_record(None, 1)

    def test_get_record_negative_id(self):
        db_repo = DatabaseRepository()
        person_record = db_repo.get_record_from_table1(-1)  # Assuming negative ID is invalid
        self.assertIsNone(person_record)

    def test_get_record_invalid_id_float(self):
        db_repo = DatabaseRepository()
        person_record = db_repo.get_record_from_table1(1.5)  # Passing float instead of integer
        self.assertIsNone(person_record)

    def test_get_record_empty_db(self):
        # Clear database and test
        from Model.models import Person,Person2

        db_repo = DatabaseRepository()
        db_repo.session.query(Person).delete()
        db_repo.session.query(Person2).delete()
        db_repo.session.commit()

        person_record = db_repo.get_record_from_table1(1)
        self.assertIsNone(person_record)

if __name__ == "__main__":
    unittest.main()