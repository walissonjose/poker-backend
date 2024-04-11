import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

db = dict(
    user=os.getenv('USER_DB'),
    password=os.getenv('PASS_DB'),
    host=os.getenv('HOST_DB'),
    port=os.getenv('PORT_DB') or 5432,
    database=os.getenv('NAME_DB'),
    schema=os.getenv('SCHEMA_DB')
)

db['url'] = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"

engine = create_engine(db['url'])
Session = sessionmaker(bind=engine)


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
