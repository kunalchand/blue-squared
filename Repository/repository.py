# repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config.config import get_db_url  # Import get_db_url to dynamically get the DB URL
from Model.models import Person, Person2
from log.log_config import setup_logger
# Set up logger for this module
logger = setup_logger("Repository")

class DatabaseRepository:
    def __init__(self):
        # Dynamically get the DB URL by calling get_db_url()
        db_url = get_db_url()
        self.engine = create_engine(db_url)
        session = sessionmaker(bind=self.engine)
        self.session = session()

        logger.info("Database connection established.")  # Log when the connection is created

    def get_record_from_table1(self, record_id):
        logger.info(f"Fetching record with ID {record_id} from table2 (Person2).")

        record = self.session.query(Person).filter(Person.id == record_id).first()

        return record

    def get_record_from_table2(self, record_id):
        logger.info(f"Fetching record with ID {record_id} from table2 (Person2).")

        record = self.session.query(Person2).filter(Person2.id == record_id).first()

        return record

    def close(self):
        self.session.close()
        logger.info("Database session closed.")  # Log when the session is closed
