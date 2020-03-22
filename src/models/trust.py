from sqlalchemy import Column, Integer, String

from src.database import DbEngine


class Trust(DbEngine.BASE):
    """
    This is a class for managing the Trust model for the database.
    """

    __tablename__ = "trusts"

    id = Column(Integer, primary_key=True)
    name = Column(String(120))

    def __repr__(self) -> str:
        return "<Trust: {}>".format(self.name)
