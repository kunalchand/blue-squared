# repository.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config.config import get_db_url  # Import get_db_url to dynamically get the DB URL
from Model.models import Person, Person2


class DatabaseRepository:
    def __init__(self):
        # Dynamically get the DB URL by calling get_db_url()
        db_url = get_db_url()
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_record_from_table1(self, record_id):
        record = self.session.query(Person).filter(Person.id == record_id).first()
        return record

    def get_record_from_table2(self, record_id):
        record = self.session.query(Person2).filter(Person2.id == record_id).first()
        return record

    def close(self):
        self.session.close()
