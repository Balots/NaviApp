from sqlalchemy.orm import Session
from app.places.models import Place
from app.places.schemas import PlaceCreate

class PlaceDAO:
    def __init__(self, db: Session):
        self.db = db

    def create(self, place: PlaceCreate):
        db_place = Place(**place.dict())
        self.db.add(db_place)
        self.db.commit()
        self.db.refresh(db_place)
        return db_place

    def get(self, place_id: int):
        return self.db.query(Place).filter(Place.id == place_id).first()

    def get_all(self):
        return self.db.query(Place).all()
