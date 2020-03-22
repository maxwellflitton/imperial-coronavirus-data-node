from unittest import main, TestCase
from mock import patch, MagicMock

from src.database import DbEngine, Singleton


class TestDbEngine(TestCase):

    @patch("config.GlobalParams")
    @patch("sqlalchemy.ext.declarative.declarative_base")
    @patch("src.database.sessionmaker")
    @patch("src.database.create_engine")
    def test___int__(self, mock_create_engine, mock_session, mock_declarative_base, mock_params):
        test = DbEngine()
        # TODO => sort out for new DB connection
        # self.assertEqual(mock_create_engine.return_value, test.engine)
        # self.assertEqual(mock_session.return_value.return_value, test.session)

        # mock_session.assert_called_once_with(bind=mock_create_engine.return_value)
        # mock_session.return_value.assert_called_once_with()

        second_test = DbEngine()
        self.assertEqual(id(second_test), id(test))
        Singleton._instances = {}

    @patch("src.models.user.User")
    @patch("src.database.DbEngine.__init__")
    def test_create_tables(self, mock_init, mock_user):
        mock_init.return_value = None
        test = DbEngine()
        test.engine = MagicMock()
        mock_user.__table__ = MagicMock()
        test.create_tables()

        mock_user.__table__.create.assert_called_once_with(bind=test.engine)


if __name__ == '__main__':
    main()
