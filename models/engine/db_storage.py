#!/usr/bin/python3
""" New Engineb DBStorage
    Using MySQLAlchemy and inherits Base class
"""

from sqlalchemy import create_engine, MetaData
from os import getenv
from models.BaseModels import Base
from sqlalchemy.orm import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ SQLAlchemy engine initiator """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                format(getenv(BNB_MYSQL_USER), getenv(HBNB_MYSQL_PWD),
                       getenv(HBNB_MYSQL_HOST), getenv(HBNB_MYSQL_DB)),
                       pool_pre_ping=True)

    def drop_tables(self):
        """
        Drops all tables 
        if the environment variable HBNB_ENV is equal to test
        """
        metadata = Metadata(bind=self.__engine)
        metadata.drop_all()
