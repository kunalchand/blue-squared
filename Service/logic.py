from log.log_config import setup_logger
from abc import ABC, abstractmethod
from Repository.repository import DatabaseRepository

logger = setup_logger("logic")


# Interface for fetcher
class Fetcher(ABC):
    @abstractmethod
    def get_record_from_table1(self, record_id):
        pass

    def get_record_from_table2(self, record_id):
        pass

#Inteface for comparison
class Compartor(ABC):
    @abstractmethod
    def compare(self, record1, record2):
        pass


# Interface for RS
class ResponseStrategy(ABC):
    @abstractmethod
    def generate_response(self, record_from_table1, record_from_table2):
        pass


# Abstraction for LOGIC
class RecordFetcher(Fetcher):
    def __init__(self, db_repo: DatabaseRepository):
        self.db_repo = db_repo

    def get_record_from_table1(self, record_id):
        logger.info(f"Fetching record from table1 with ID {record_id}.")
        return self.db_repo.get_record_from_table1(record_id)

    def get_record_from_table2(self, record_id):
        logger.info(f"Fetching record from table2 with ID {record_id}.")
        return self.db_repo.get_record_from_table2(record_id)


# Extra Abstraction for separation of Concerns
class RecordFetcherService:
    def __init__(self, record_fetcher: RecordFetcher):
        self.record_fetcher = record_fetcher

    def fetch_record_from_table1(self, record_id):
        return self.record_fetcher.get_record_from_table1(record_id)

    def fetch_record_from_table2(self, record_id):
        return self.record_fetcher.get_record_from_table2(record_id)


# Abstraction for logic compare
class RecordComparer(Compartor):
    def compare(self, record1, record2):
        same_fields = {}
        different_fields = {}

        logger.info(f"Comparing records.")
        for column in record1.__table__.columns:
            field_name = column.name
            value1 = getattr(record1, field_name)
            value2 = getattr(record2, field_name)

            if value1 == value2:
                same_fields[field_name] = value1
            else:
                different_fields[field_name] = {"Table1_value": value1, "Table2_Value": value2}

        return {"same_fields": same_fields, "different_fields": different_fields}


# Extra Abstraction for separation of Concerns

class RecordComparisonService:
    def __init__(self, record_comparer: RecordComparer):
        self.record_comparer = record_comparer

    def compare_records(self, record1, record2):
        return self.record_comparer.compare(record1, record2)

#Defining Reponse

class Response(ResponseStrategy):
    def generate_response(self, record_from_table1, record_from_table2):
        response = {}

        if record_from_table1:
            logger.info(f"Adding record from Table 1: {record_from_table1}")
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name,
                                  'gender': record_from_table1.gender,
                                  'height': record_from_table1.height_cm, 'city': record_from_table1.city}
        else:
            logger.warning("No record found in Table 1")

        if record_from_table2:
            logger.info(f"Adding record from Table 2: {record_from_table2}")
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name,
                                  'gender': record_from_table2.gender,
                                  'height': record_from_table2.height_cm, 'city': record_from_table2.city}
        else:
            logger.warning("No record found in Table 2")

        return response


class RecordService:
    def __init__(self, fetch_strategy: RecordFetcherService, compare_strategy: RecordComparisonService,
                 response_strategy: Response):
        self.fetch_strategy = fetch_strategy
        self.compare_strategy = compare_strategy
        self.response_strategy = response_strategy
        logger.info("RecordService initialized with FetchStrategy, ComparisonStrategy, and ResponseStrategy")

    def get_records_single_id(self, record_id):
        logger.info(f"Fetching records for a single ID: {record_id}")
        logger.info(f"Fetching records for IDs: {record_id}")

        # Fetch records using the strategy
        record_from_table1 = self.fetch_strategy.fetch_record_from_table1(record_id)
        logger.info(f"Record from Table 1 (ID: {record_id}): record_from_table1")

        record_from_table2 = self.fetch_strategy.fetch_record_from_table2(record_id)
        logger.info(f"Record from Table 2 (ID: {record_id}): record_from_table2")

        # Generate the response using the strategy
        response = self.response_strategy.generate_response(record_from_table1, record_from_table2)
        logger.info(f"Generated response: {response}")

        # Compare records using the strategy
        comparison = self.compare_strategy.compare_records(record_from_table1, record_from_table2)
        logger.info(f"Comparison result: {comparison}")

        response["Comparison"] = comparison
        return response

    def get_records(self, record_id1, record_id2):
        logger.info(f"Fetching records for IDs: {record_id1} and {record_id2}")

        # Fetch records using the strategy
        record_from_table1 = self.fetch_strategy.fetch_record_from_table1(record_id1)
        logger.info(f"Record from Table 1 (ID: {record_id1}): {record_from_table1}")

        record_from_table2 = self.fetch_strategy.fetch_record_from_table2(record_id2)
        logger.info(f"Record from Table 2 (ID: {record_id2}): {record_from_table2}")

        # Generate the response using the strategy
        response = self.response_strategy.generate_response(record_from_table1, record_from_table2)
        logger.info(f"Generated response: {response}")

        # Compare records using the strategy
        comparison = self.compare_strategy.compare_records(record_from_table1, record_from_table2)
        logger.info(f"Comparison result: {comparison}")

        response["Comparison"] = comparison
        return response


db_repo = DatabaseRepository()
fetcher = RecordFetcher(db_repo)
fetch = RecordFetcherService(fetcher)
comparer = RecordComparer()
compare = RecordComparisonService(comparer)
response = Response()
