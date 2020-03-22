import os
import sys
import unittest
from mock import patch
import tempfile

from run import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        # with app.app_context():
        #     import_models(database=db)

    def tearDown(self):
        os.close(self.db_fd)
        # os.remove("test.db")
        os.unlink(app.config['DATABASE'])

    def test_home(self):
        self.assertEqual(200, self.app.get("/")._status_code)

    def test_users(self):
        self.assertEqual(200, self.app.get("/users/")._status_code)
        self.assertEqual(200, self.app.get("/users/login")._status_code)
        # self.assertEqual(200, self.app.get("/users/register")._status_code)


if __name__ == '__main__':
    unittest.main()
