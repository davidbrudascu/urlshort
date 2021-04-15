from .db import Base 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Urls(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    short_url = Column(String, index=True)
    
    


