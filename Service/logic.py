import logging

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


    def get_fields_from_both_tables(self, record_id):
        logger.info(f"Fetching records from both tables on ID {record_id} from Both tables (Person,Person2).")
        return self.db_repo.get_same_different_from_tables(record_id)

    def get_fields_from_both_tables2(self,record_id1,record_id2):
        logger.info(f"Fetching records from both tables on Different IDs{record_id1},{record_id2} "
                    f"from Both tables (Person,Person2).")
        return self.db_repo.get_same_different_from_tables_2(record_id1,record_id2)

    #  method to fetch records based on two IDs from both tables
    def get_records(self, record_id1, record_id2):
        # Fetch records from both tables using the two different IDs
        record_from_table1 = self.get_record_from_table1(record_id1)
        record_from_table2 = self.get_record_from_table2(record_id2)
        response = {}

        logger.info(f"Call the get_records() method to check whether Both Records present or not")

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name, 'gender':record_from_table1.gender,
                                  'height':record_from_table1.height_cm, 'city':record_from_table1.city}
            logger.info(f"Successfully record {record_id1} exists in table1(Person) in required format")
        else:
            response['table1'] = None
            logger.info(f"Record {record_id1} is not available in the table1(Person)")

        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name, 'gender':record_from_table2.gender,
                                  'height':record_from_table2.height_cm, 'city':record_from_table2.city}
            logger.info(f"Successfully record {record_id2} exists in table2(Person2) in required format")

        else:
            response['table2'] = None
            logger.info(f"Record {record_id2} is not available in the table1(Person)")


        logger.info("Now calling the comparison function to get the same/different fields for both sets of records of "
                    "table1")

        comparison_result1 = self.get_fields_from_both_tables2(record_id1,record_id2)
        response['comparison1'] = comparison_result1
        logger.info(f"Adding the comparison results from different id there are {record_id1},{record_id2} to the response")
        return response


    #  method to fetch records based on a single ID from both tables
    def get_records_single_id(self, record_id):

        logger.info(f"Call the get_records_single_id() method to check whether Both Records present or not by passing Id {record_id}")

        # Fetch records from both tables using the single ID
        record_from_table1 = self.get_record_from_table1(record_id)
        record_from_table2 = self.get_record_from_table2(record_id)

        response = {}

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name, 'gender':record_from_table1.gender,
                                  'height':record_from_table1.height_cm, 'city':record_from_table1.city}
            logger.info(f"Successfully record {record_id} exists in table1(Person) in required format")

        else:
            response['table1'] = None
            logger.info(f"Record {record_id} is not available in the table1(Person)")


        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name, 'gender':record_from_table2.gender,
                                  'height':record_from_table2.height_cm, 'city':record_from_table2.city}
            logger.info(f"Successfully record {record_id} exists in table2(Person) in required format")

        else:
            response['table2'] = None
            logger.info(f"Record {record_id} is not available in the table1(Person)")



        logger.info(f"Now calling the comparison function get_records_single_id() to get the fields on ID {record_id}")
        comparison_result = self.get_fields_from_both_tables(record_id)

        # Add the comparison result to the response
        response['comparison2'] = comparison_result

        logger.info(f"Adding the comparison results on Same id {record_id} to the response")

        return response
