from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    
def start_application ():
    app=FastAPI(title=settings.PEROJECT_TITLE,version=settings.PEROJECT_VERSION)
    create_tables() 
    return app
 

app=start_application()

app.get("/")
def hello_api():
    return {"details":"hello world"}
