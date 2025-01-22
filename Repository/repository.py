import sys
import os

# Add the project root directory (blue-squared) to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
sys.path.append(project_root)

# Now import the repository from the Repository folder
from Model.models import Person, Person2
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DatabaseRepository:
    def __init__(self, db_url):
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
