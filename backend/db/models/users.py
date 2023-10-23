from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class User(Base):
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False,unique=True,index=True)
    email=Column(String,nullable=False)
    ia_active=Column(Boolean(),default=True)
    is_superuser=Column(Boolean(),default=False)
    jobs=relationship("Job",back_populates="owner")