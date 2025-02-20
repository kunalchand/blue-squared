from log.log_config import setup_logger
from abc import ABC, abstractmethod
from Service.RecordFetcherandComapritor import RecordFetcherAndComparer,response,compare,fetch

logger = setup_logger("logic")


class IRecordService:
    @abstractmethod
    def get_records_single_id(self, record_id):
        pass

    @abstractmethod
    def get_records(self, record_id1, record_id2):
        pass


class RecordService(IRecordService):
    def __init__(self, fetcher_and_comparer: RecordFetcherAndComparer):
        self.fetcher_and_comparer = fetcher_and_comparer
        logger.info("RecordService initialized with RecordFetcherAndComparer")

    def get_records_single_id(self, record_id):
        return self.fetcher_and_comparer.fetch_and_compare_records(record_id)

    def get_records(self, record_id1, record_id2):
        return self.fetcher_and_comparer.fetch_and_compare_records(record_id1, record_id2)


Records = RecordFetcherAndComparer(fetch, compare, response)


