from abc import ABC, abstractmethod
from log.log_config import setup_logger
logger = setup_logger("RecordCompartor(Service)")



# Interface for RS
class ResponseStrategy(ABC):
    @abstractmethod
    def generate_response(self, record_from_table1, record_from_table2):
        pass

# Defining Response
class Response(ResponseStrategy):
    def generate_response(self, record_from_table1, record_from_table2):
        response = {}

        if record_from_table1:
            logger.info(f"Adding record from Table 1: record_from_table1")
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name,
                                  'gender': record_from_table1.gender,
                                  'height': record_from_table1.height_cm, 'city': record_from_table1.city}
        else:
            logger.warning("No record found in Table 1")

        if record_from_table2:
            logger.info(f"Adding record from Table 2: record_from_table2")
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name,
                                  'gender': record_from_table2.gender,
                                  'height': record_from_table2.height_cm, 'city': record_from_table2.city}
        else:
            logger.warning("No record found in Table 2")

        return response
