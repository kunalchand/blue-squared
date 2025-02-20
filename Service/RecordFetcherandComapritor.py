from Service.RecordFetcher import RecordFetcherService,fetcher
from Service.RecordsComapartor import RecordComparisonService, comparer
from Service.ResponseGenerator import Response
from log.log_config import setup_logger
from abc import ABC, abstractmethod


logger = setup_logger("RecordFetcherAndCompartor")



class IRecordFetcherAndComparer(ABC):
    @abstractmethod
    def fetch_and_compare_records(self,record_id):
        pass


class RecordFetcherAndComparer(IRecordFetcherAndComparer):
    def __init__(self, fetch_strategy: RecordFetcherService, compare_strategy: RecordComparisonService,
                 response_strategy: Response):
        self.fetch_strategy = fetch_strategy
        self.compare_strategy = compare_strategy
        self.response_strategy = response_strategy

    def fetch_and_compare_records(self, *record_ids):
        try:
            if len(record_ids) == 1:
                record_id1 = record_ids[0]
                # Fetch records using the same ID for both tables
                record_from_table1 = self.fetch_strategy.fetch_record_from_table1(record_id1)
                record_from_table2 = self.fetch_strategy.fetch_record_from_table2(record_id1)
                logger.info(f"Using the same ID for both tables (ID: {record_id1})")
            elif len(record_ids) == 2:
                record_id1, record_id2 = record_ids
                # Fetch records using ID1 for Table 1 and ID2 for Table 2
                record_from_table1 = self.fetch_strategy.fetch_record_from_table1(record_id1)
                record_from_table2 = self.fetch_strategy.fetch_record_from_table2(record_id2)
                logger.info(f"Using different IDs for tables (ID1: {record_id1}, ID2: {record_id2})")
            else:
                raise ValueError("You must provide either 1 or 2 record IDs.")

            # Generate the response using the strategy
            response = self.response_strategy.generate_response(record_from_table1, record_from_table2)
            logger.info(f"Generated response: {response}")

            # Compare records using the strategy
            comparison = self.compare_strategy.compare_records(record_from_table1, record_from_table2)
            logger.info(f"Comparison result: {comparison}")

            response["Comparison"] = comparison
            return response
        except Exception as e:
            logger.error(f"Error while fetching and comparing records: {str(e)}")
            return {"message": str(e)}, 500


fetch = RecordFetcherService(fetcher)
compare = RecordComparisonService(comparer)
response = Response()
