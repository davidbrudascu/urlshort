from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .db import SessionLocal, engine
from .randomgen import random


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency 

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.get("/")
def root():
    return {"message": "Casandrova"}

@app.post("/urls/", response_model=schemas.Url)
def create_url(urls: schemas.UrlBase, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_id(db = db, url_id = 200)
    if db_url:
        raise HTTPException(status_code=400, detail="Id already registered")
    return crud.create_long_url(db = db, items = urls)