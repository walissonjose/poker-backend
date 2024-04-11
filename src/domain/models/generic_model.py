from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from config.database import db

metadata = MetaData(schema="app_poker")
Base = declarative_base(metadata=metadata)


class GenericModel(Base):
    __abstract__ = True
