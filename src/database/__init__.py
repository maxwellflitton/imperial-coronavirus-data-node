from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import GlobalParams
from src.singleton import Singleton
params = GlobalParams()


class DbEngine(metaclass=Singleton):
    """
    This is an class for managing the connection and sessions to the database.
    Attributes:
        engine (sqlalchemy.create_engine.return_value): connection to DB
        session (sqlalchemy.orm.sessionmaker.return_value): manages sessions with database
    """
    BASE = declarative_base()

    def __init__(self):
        """
        The constructor for the DbEngine class.
        """
        self.engine = create_engine(params.get("DB_URL"), echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        """
        Creates tables for the database.

        :return: None
        """
        from src.models.trust import Trust
        from src.models.user import User
        Trust.__table__.create(bind=self.engine)
        User.__table__.create(bind=self.engine)
