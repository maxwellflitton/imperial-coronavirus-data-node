from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from werkzeug.security import generate_password_hash
from uuid import uuid4

from src.database import DbEngine


class User(DbEngine.BASE):
    """
    This is a class for managing the User model for the database.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    unique_id = Column(String(120), unique=True)
    credit_amount = Column(Integer, default=0, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128))
    admin = Column(Boolean(), default=False)
    trust_id = Column(Integer, ForeignKey("trusts.id"), nullable=False)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the password for checking and being saved.
        :param password: (str) password to be hashed
        :return: (str) hashed password
        """
        return generate_password_hash(password=password)

    def check_password(self, password: str) -> bool:
        """
        Checks the password to see if it matches the User's password.
        :param password: (str) password to be checked
        :return: True is matched => False if not
        """
        if self.hash_password(password=password) == self.password:
            return True
        return False

    def save_instance(self) -> None:
        """
        Saves instance to database.
        :return: None
        """
        # TODO: put into __init__
        self.password = self.hash_password(password=self.password)
        self.unique_id = str(uuid4())
        database = DbEngine()
        database.session.add(self)
        database.session.commit()

    def __repr__(self):
        return "<User {}>".format(self.username)
