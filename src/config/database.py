import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

db = dict(
    user=os.getenv('USER_DB'),
    password=os.getenv('PASSWORD_DB'),
    host=os.getenv('HOST_DB'),
    port=os.getenv('PORT_DB') or 5432,
    database=os.getenv('DATABASE_DB'),
    schema=os.getenv('SCHEMA_DB')
)

db['url'] = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"

engine = create_engine(db['url'])
Session = sessionmaker(bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
