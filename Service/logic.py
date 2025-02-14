from abc import ABC, abstractmethod
from log.log_config import setup_logger
from Repository.repository import DatabaseRepository

logger = setup_logger("logic")


class IDataFetcher(ABC):
    @abstractmethod
    def get_record(self, record_id):
        pass


class DatabaseRecordFetcher(IDataFetcher):
    def __init__(self, db_repo: DatabaseRepository):
        self.db_repo = db_repo

    def get_record(self, record_id):
        # Fetch the record from the database
        record_from_table1 = self.db_repo.get_record_from_table1(record_id)
        record_from_table2 = self.db_repo.get_record_from_table2(record_id)
        return {"table1": record_from_table1, "table2": record_from_table2}


class IRecordComparator(ABC):
    @abstractmethod
    def compare(self, record_from_table1, record_from_table2):
        pass


class RecordComparator(IRecordComparator):
    def compare(self, record_from_table1, record_from_table2):
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

        return {"same_fields": same_fields, "different_fields": different_fields}


class RecordService:
    def __init__(self):
        self.db_repo = DatabaseRepository()
        self.fetcher = DatabaseRecordFetcher(self.db_repo)
        self.comparator = RecordComparator()

    def fetch_records(self, record_id):
        records = self.fetcher.get_record(record_id)
        return records

    def prepare_response(self, records, record_id):
        response = {}

        table1_record = records["table1"]
        table2_record = records["table2"]

        logger.info(f"Fetching records for ID {record_id}")

        # Prepare response for table1
        if table1_record:
            response['table1'] = {'id': table1_record.id, 'name': table1_record.name,
                                  'gender': table1_record.gender,
                                  'height': table1_record.height_cm, 'city': table1_record.city}
            logger.info(f"Record {record_id} exists in table1 (Person)")
        else:
            response['table1'] = None
            logger.info(f"Record {record_id} not found in table1 (Person)")

        # Prepare response for table2
        if table2_record:
            response['table2'] = {'id': table2_record.id, 'name': table2_record.name,
                                  'gender': table2_record.gender,
                                  'height': table2_record.height_cm, 'city': table2_record.city}
            logger.info(f"Record {record_id} exists in table2 (Person2)")
        else:
            response['table2'] = None
            logger.info(f"Record {record_id} not found in table2 (Person2)")

        return response

    def compare_records(self, records, record_id):
        table1_record = records["table1"]
        table2_record = records["table2"]
        response = {}

        if table1_record and table2_record:
            comparison_result = self.comparator.compare(table1_record, table2_record)
            response["Comparison"] = comparison_result
            logger.info(f"Comparison completed for ID {record_id}")
        else:
            logger.warning(f"Cannot compare, one or both records not found for ID {record_id}")

        return response

    def get_records_single_id(self, record_id):
        records = self.fetch_records(record_id)
        response = self.prepare_response(records, record_id)
        comparison = self.compare_records(records, record_id)
        response.update(comparison)
        return response

    def get_records_multiple_ids(self, record_id1, record_id2):
        records1 = self.fetch_records(record_id1)
        records2 = self.fetch_records(record_id2)

        response = {
            "table1": self.prepare_response(records1, record_id1),
            "table2": self.prepare_response(records2, record_id2),
        }

        comparison = self.compare_records({"table1": records1["table1"], "table2": records2["table2"]},
                                          f"{record_id1} and {record_id2}")
        response.update(comparison)

        return response
