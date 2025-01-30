from test_base import BaseTestCase

class TestGetMultipleRecords(BaseTestCase):
    def test_get_records_valid(self):
        # Test with two existing records in the database (no insertion, assume they already exist)
        response = self.client.get('/get_records/1/2')
        self.assertEqual(response.status_code, 200)  # Check if status code is 200

        data = response.get_json()

        # Check if both records from table1 and table2 exist in the response
        self.assertIsNotNone(data.get('table1'))
        self.assertIsNotNone(data.get('table2'))

        # Check if the content is correct for table1 (Person table) for ID 1
        table1_data = data.get('table1')
        self.assertEqual(table1_data['id'], 1)
        self.assertEqual(table1_data['name'], 'John Doe')
        self.assertEqual(table1_data['gender'], 'Male')
        self.assertEqual(table1_data['height'], 180)
        self.assertEqual(table1_data['city'], 'New York')

        # Check if the content is correct for table2 (Person2 table) for ID 2
        table2_data = data.get('table2')
        self.assertEqual(table2_data['id'], 2)
        self.assertEqual(table2_data['name'], 'Sophia Lee')
        self.assertEqual(table2_data['gender'], 'Female')
        self.assertEqual(table2_data['height'], 158)
        self.assertEqual(table2_data['city'], 'Seattle')
