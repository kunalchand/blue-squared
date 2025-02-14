
from Repository.repository import DatabaseRepository
from log.log_config import setup_logger

logger = setup_logger("logic")

class RecordService:
    def __init__(self):
        self.db_repo = DatabaseRepository()

    logger.info("Retrieving Data from Repository to Service Logic")


    def get_record_from_table1(self, record_id):
        # Fetch record from table1 (Person)
        logger.info(f"Masking record from fetched data ID {record_id} from table1 (Person).")
        return self.db_repo.get_record_from_table1(record_id)


    def get_record_from_table2(self, record_id):
        # Fetch record from table2 (Person2)
        logger.info(f"Masking record from fetched data ID {record_id} from table2 (Person2).")
        return self.db_repo.get_record_from_table2(record_id)


    def get_records_single_id(self, record_id):
        # Fetch records from both tables using the same IDs
        record_from_table1 = self.get_record_from_table1(record_id)
        record_from_table2 = self.get_record_from_table2(record_id)
        response = {}

        logger.info(f"Call the get_records_single_id() method to check whether Both Records present or not")

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name, 'gender' :record_from_table1.gender,
                                  'height' :record_from_table1.height_cm, 'city' :record_from_table1.city}
            logger.info(f"Successfully record {record_id} exists in table1(Person) in required format")
        else:
            response['table1'] = None
            logger.info(f"Record {record_id} is not available in the table1(Person)")

        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name, 'gender' :record_from_table2.gender,
                                  'height' :record_from_table2.height_cm, 'city' :record_from_table2.city}
            logger.info(f"Successfully record {record_id} exists in table2(Person2) in required format")

        else:
            response['table2'] = None
            logger.info(f"Record {record_id} is not available in the table2(Person2)")

        same_fields = {}
        different_fields ={}
        logger.info(f"Comparison is initiated for IDs {record_id}")
        for column in record_from_table1.__table__.columns:
            field_name = column.name
            value1 = getattr(record_from_table1, field_name)
            value2 = getattr(record_from_table2, field_name)

            if value1 == value2:
                same_fields[field_name] = value1
            else:
                different_fields[field_name] = {" Table1_value ": value1, " Table2_Value ": value2}
        logger.info("compared both fields separating in to same and different fields add upto Response ")
        response["Comparison"] = {"same_fields": same_fields, "different_fields": different_fields}

        return response

    def get_records(self, record_id1, record_id2):
        # Fetch records from both tables using the two different IDs
        record_from_table1 = self.get_record_from_table1(record_id1)
        record_from_table2 = self.get_record_from_table2(record_id2)
        response = {}

        logger.info(f"Call the get_records() method to check whether Both Records present or not")

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name,
                                  'gender': record_from_table1.gender,
                                  'height': record_from_table1.height_cm, 'city': record_from_table1.city}
            logger.info(f"Successfully record {record_id1} exists in table1(Person) in required format")
        else:
            response['table1'] = None
            logger.info(f"Record {record_id1} is not available in the table1(Person)")

        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name,
                                  'gender': record_from_table2.gender,
                                  'height': record_from_table2.height_cm, 'city': record_from_table2.city}
            logger.info(f"Successfully record {record_id2} exists in table2(Person2) in required format")

        else:
            response['table2'] = None
            logger.info(f"Record {record_id2} is not available in the table2(Person)")

        logger.info(f"Comparison Is Initiated between IDs {record_id1} and {record_id2}")

        same_fields = {}
        different_fields = {}

        for column in record_from_table1.__table__.columns:
            field_name = column.name
            value1 = getattr(record_from_table1, field_name)
            value2 = getattr(record_from_table2, field_name)

            if value1 == value2:
                same_fields[field_name] = value1
            else:
                different_fields[field_name] = {" Table1_value ": value1, " Table2_Value ": value2}

        logger.info("compared both fields separating in to same and different fields add upto Response ")

        response["Comparison"] = {"same_fields": same_fields, "different_fields": different_fields}

        return response