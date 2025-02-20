from abc import ABC, abstractmethod
from log.log_config import setup_logger
logger = setup_logger("RecordCompartor(Service)")



# Inteface for comparison
class Compartor(ABC):
    @abstractmethod
    def compare(self, record1, record2):
        pass

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


comparer = RecordComparer()
