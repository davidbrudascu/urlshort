from typing import List, Optional
from pydantic import BaseModel
import datetime

class UrlBase(BaseModel):
    long_url: str
    short_url: str
    

class Url(UrlBase):
    id: int
    
    class Config:
        orm_mode = True