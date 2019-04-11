from app import app, db
import unittest

class TestDatabase(unittest.TestCase):

    def setup(self):
        # link to the db
        pass

     def test_add_valid(self):
         response = self.app.post('/add', data = {"form": {"expression":"1+1"}},follow_redirects=True)
         self.assertEqual(response.status_code, 200)

    def test_add_invalid(self):
        response = self.app.post('/add', data = {"form": {"expression":"1+"}},follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        # tear down the db
        pass
