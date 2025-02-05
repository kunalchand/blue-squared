# repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config.config import get_db_url  # Import get_db_url to dynamically get the DB URL
from Model.models import Person, Person2
from log.log_config import setup_logger
logger = setup_logger("Repository")


class DatabaseRepository:
    def __init__(self):
        # Dynamically get the DB URL by calling get_db_url()
        db_url = get_db_url()
        self.engine = create_engine(db_url)
        session = sessionmaker(bind=self.engine)
        self.session = session()

        logger.info("Database connection established.")
        
    def get_record_from_table1(self, record_id):
        logger.info(f"Fetching record with ID {record_id} from table2 (Person2).")

        record = self.session.query(Person).filter(Person.id == record_id).first()

        return record

    def get_record_from_table2(self, record_id):
        logger.info(f"Fetching record with ID {record_id} from table2 (Person2).")

        record = self.session.query(Person2).filter(Person2.id == record_id).first()

        return record

    def get_same_different_from_tables(self, record_id):
        logger.info(f"Fetching records from both tables with ID {record_id} to compare fields.")

        record1 = self.session.query(Person).filter(Person.id == record_id).first()
        record2 = self.session.query(Person2).filter(Person2.id == record_id).first()

        # If one of the records is not found, return an empty result
        if not record1 or not record2:
            logger.warning("One or both records not found.")
            return {}

        # Compare fields
        same_fields = {}
        different_fields = {}

        # Assuming you are comparing all fields (adjust based on your actual fields)
        for column in record1.__table__.columns:
            field_name = column.name
            value1 = getattr(record1, field_name)
            value2 = getattr(record2, field_name)

            if value1 == value2:
                same_fields[field_name] = value1
            else:
                different_fields[field_name] = {'table1_value': value1, 'table2_value': value2}

        return {
            "same_fields": same_fields,
            "different_fields": different_fields
        }

    def get_same_different_from_tables_2(self, record_id1, record_id2):
        logger.info(f"Fetching records from both tables with ID {record_id1} from Person Table with ID {record_id2}"
                    f" from Person2 to compare fields.")

        record1 = self.session.query(Person).filter(Person.id == record_id1).first()
        record2 = self.session.query(Person2).filter(Person2.id == record_id2).first()

        # If one of the records is not found, return an empty result
        if not record1 or not record2:
            logger.warning("One or both records not found.")
            return {}

        # Compare fields
        same_fields = {}
        different_fields = {}

        # Assuming you are comparing all fields (adjust based on your actual fields)
        for column in record1.__table__.columns:
            field_name = column.name
            value1 = getattr(record1, field_name)
            value2 = getattr(record2, field_name)

            if value1 == value2:
                same_fields[field_name] = value1
            else:
                different_fields[field_name] = {'table1_value': value1, 'table2_value': value2}

        return {
            "same_fields": same_fields,
            "different_fields": different_fields
        }
