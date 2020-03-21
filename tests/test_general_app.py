import os
import sys
import unittest
from mock import patch
import tempfile

from run import app, db, import_models


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config["TEMPLATE_FOLDER"] = 'src/templates'
        self.app = app.test_client()
        with app.app_context():
            import_models(database=db)

    def tearDown(self):
        os.close(self.db_fd)
        os.remove("test.db")
        os.unlink(app.config['DATABASE'])

    def test_home(self):
        self.assertEqual(200, self.app.get("/")._status_code)

    def test_users(self):
        self.assertEqual(200, self.app.get("/users/")._status_code)
        self.assertEqual(200, self.app.get("/users/login")._status_code)


if __name__ == '__main__':
    unittest.main()
