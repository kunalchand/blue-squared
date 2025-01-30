# tests/test_base.py
import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import create_app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Create a Flask test client
        self.app = create_app()
        self.client = self.app.test_client()
