from sqlalchemy.orm import Session

from . import models, schemas, randomgen

def get_urls(db: Session, url_id: int):
    return db.query(models.Urls).filter(models.Urls.id == url_id).first()

def get_url_by_id(db: Session, url_id: int):
    return db.query(models.Urls).filter(models.Urls.id == url_id).first()

def create_long_url(db : Session, items: schemas.UrlBase):
    random_number = randomgen.generate_random()
    db_item = models.Urls(long_url = items.long_url, short_url = random_number)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
