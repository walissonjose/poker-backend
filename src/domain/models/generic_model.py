from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config.database import db

metadata = db.MetaData(schema=db['schema'])
Base = declarative_base()


class GenericModel(Base):
    __abstract__ = True
