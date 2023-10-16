from typing import Any
from sqlalchemy.ext.declarative import as_declarative,declared_attr


@as_declarative()
class Base:
    __name__:str

    def __tablename(cls)->str:
        return cls.__name__.lower()
    
