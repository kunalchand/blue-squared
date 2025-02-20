from abc import ABC, abstractmethod
from log.log_config import setup_logger
logger = setup_logger("RecordFetcher(Service)")
from Repository.repository import DatabaseRepository

class Fetcher(ABC):
    @abstractmethod
    def get_record_from_table1(self, record_id):
        pass
    @abstractmethod
    def get_record_from_table2(self, record_id):
        pass



# Abstraction for LOGIC
class RecordFetcher(Fetcher):
    def __init__(self, db_repo: Fetcher):
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
        logger.info(f"Masking record from Record Fetcher Class with Table 1 ID {record_id}.")
        return self.record_fetcher.get_record_from_table1(record_id)

    def fetch_record_from_table2(self, record_id):
        logger.info(f"Masking record from Record Fetcher Class with Table 2 ID {record_id}.")
        return self.record_fetcher.get_record_from_table2(record_id)

db_repo = DatabaseRepository()
fetcher = RecordFetcher(db_repo)