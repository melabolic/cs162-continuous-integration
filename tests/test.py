from app import app, db
import unittest

class TestDatabase(unittest.TestCase):

    def test_add_valid(self):
        '''tests for valid inputs'''
        response = self.app.post('/add', data = {"form": {"expression":"1+1"}},follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_invalid(self):
        '''tests for invalid inputs'''
        response = self.app.post('/add', data = {"form": {"expression":"1+"}},follow_redirects=True)
        self.assertEqual(response.status_code, 400)
