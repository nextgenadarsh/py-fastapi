# db connection related stuff
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from api.auth.router import get_user
from api.database import Base, get_db
from main import app

DATABASE_URL = 'sqlite:///./db//fastapi-test.db'

engine = create_engine(DATABASE_URL, 
                       connect_args={'check_same_thread': False },
                       poolclass=StaticPool
                       )

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db_override():
    db: Session = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
