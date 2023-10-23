from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

sqlalchemy_Database_URL=settings.DATABASE_URL
engine=create_engine(sqlalchemy_Database_URL)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db()->Generator:
    try:
        db=sessionlocal()
        yield db
    finally :
        db.close()    

