from Repository.repository import DatabaseRepository

class RecordService:
    def __init__(self):
        self.db_repo = DatabaseRepository()

    def get_record_from_table1(self, record_id):
        # Fetch record from table1 (Person)
        return self.db_repo.get_record_from_table1(record_id)

    def get_record_from_table2(self, record_id):
        # Fetch record from table2 (Person2)
        return self.db_repo.get_record_from_table2(record_id)

    #  method to fetch records based on two IDs from both tables
    def get_records(self, record_id1, record_id2):
        # Fetch records from both tables using the two different IDs
        record_from_table1 = self.get_record_from_table1(record_id1)
        record_from_table2 = self.get_record_from_table2(record_id2)

        response = {}

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name, 'gender':record_from_table1.gender,
                                  'height':record_from_table1.height_cm, 'city':record_from_table1.city}
        else:
            response['table1'] = None

        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name, 'gender':record_from_table2.gender,
                                  'height':record_from_table2.height_cm, 'city':record_from_table2.city}
        else:
            response['table2'] = None

        return response

    #  method to fetch records based on a single ID from both tables
    def get_records_single_id(self, record_id):
        # Fetch records from both tables using the single ID
        record_from_table1 = self.get_record_from_table1(record_id)
        record_from_table2 = self.get_record_from_table2(record_id)

        response = {}

        # If record exists in table 1
        if record_from_table1:
            response['table1'] = {'id': record_from_table1.id, 'name': record_from_table1.name, 'gender':record_from_table1.gender,
                                  'height':record_from_table1.height_cm, 'city':record_from_table1.city}
        else:
            response['table1'] = None

        # If record exists in table 2
        if record_from_table2:
            response['table2'] = {'id': record_from_table2.id, 'name': record_from_table2.name, 'gender':record_from_table2.gender,
                                  'height':record_from_table2.height_cm, 'city':record_from_table2.city}
        else:
            response['table2'] = None

        return response
