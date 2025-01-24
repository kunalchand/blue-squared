# logic.py

from Repository.repository import DatabaseRepository

class RecordService:
    def __init__(self):
        self.db_repo = DatabaseRepository()

    def get_records(self, record_id):
        record_from_table1 = self.db_repo.get_record_from_table1(record_id)
        record_from_table2 = self.db_repo.get_record_from_table2(record_id)

        response = {}

        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name}
        else:
            response['table1'] = None

        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name}
        else:
            response['table2'] = None

        return response

    def close(self):
        self.db_repo.close()
