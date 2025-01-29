import unittest
from app import create_app


class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a Flask test client
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_records_single_id_valid(self):
        # Assuming ID 1 exists in both tables
        response = self.client.get('/get_records/1')
        self.assertEqual(response.status_code, 200)  # Check if status code is 200

        data = response.get_json()

        # Check if both records from table1 and table2 exist in the response
        self.assertIsNotNone(data.get('table1'))
        self.assertIsNotNone(data.get('table2'))

    def test_get_records__valid(self):
        # Assuming ID 1 exists in both tables
        response = self.client.get('/get_records/1/2')
        self.assertEqual(response.status_code, 200)  # Check if status code is 200

        data = response.get_json()

        # Check if both records from table1 and table2 exist in the response
        self.assertIsNotNone(data.get('table1'))
        self.assertIsNotNone(data.get('table2'))

if __name__ == '__main__':
    unittest.main()
