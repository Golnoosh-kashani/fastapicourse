from fastapi import FastAPI
from core.config import settings
app=FastAPI(title=settings.PEROJECT_TITLE,version=settings.PEROJECT_VERSION)

app.get("/")
def hello_api():
    return {"details":"hello world"}
