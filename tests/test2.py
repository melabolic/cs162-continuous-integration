# code take from https://gist.github.com/kevinyang372/252c0f5a0d37fbef478d6774ef185603?fbclid=IwAR1bGvZwDy16Wod6dnERFKed1qJGfROgscJmJEavOCDbj0lqoAIfUmqRFdw
import os
import requests
import unittest
from sqlalchemy import create_engine

class DockerComposeTestCase(unittest.TestCase):

    def test_endpoint(self):
        '''Tests if valid entries get added to the DB'''
        r = requests.post('http://127.0.0.1:5000/add', data={'expression':'100+100'})
        self.assertEqual(r.status_code, 200)

    def test_error_endpoint(self):
        '''Tests if invalid entries get added to the DB'''
        r = requests.post('http://127.0.0.1:5000/add', data={'expression':'100+'})
        self.assertNotEqual(r.status_code, 200)

    def test_db(self):
        '''Tests if DB records valid post requests'''
        r = requests.post('http://127.0.0.1:5000/add', data={'expression':'100+100'})
        engine = create_engine('postgresql://cs162_user:cs162_password@127.0.0.1:5432/cs162', echo = True)

        with engine.connect() as con:
            rs = con.execute("SELECT * FROM Expression WHERE text = '100+100'")
            rows = rs.fetchall()

        self.assertNotEqual(len(rows), 0)

    def test_error_db(self):
        '''Tests if DB records invalid post requests'''
        r = requests.post('http://127.0.0.1:5000/add', data={'expression':'100+'})
        engine = create_engine('postgresql://cs162_user:cs162_password@127.0.0.1:5432/cs162', echo = True)

        with engine.connect() as con:
            rs = con.execute("SELECT * FROM Expression WHERE text = '100+'")
            rows = rs.fetchall()

        self.assertEqual(len(rows), 0)

if __name__ == '__main__':
    unittest.main()
