from werkzeug.security import generate_password_hash
from uuid import uuid4
from flask_login import UserMixin

from run import db


class User(db.Model):
    """
    This is a class for managing the User model for the database.
    """

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(120), unique=True)
    credit_amount = db.Column(db.Integer, default=0, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))

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
        self.password = self.hash_password(password=self.password)
        self.unique_id = uuid4()
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<User {}>".format(self.username)
