from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies.dao_dep import get_db
from place_dao import PlaceDAO
from .schemas import PlaceCreate, PlaceRead
from .yandex_maps import search_places, extract_places

router = APIRouter(
    prefix="/places",
    tags=["places"],
)

@router.post("/", response_model=PlaceRead)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    place_dao = PlaceDAO(db)
    return place_dao.create(place)

@router.get("/{place_id}", response_model=PlaceRead)
def read_place(place_id: int, db: Session = Depends(get_db)):
    place_dao = PlaceDAO(db)
    place = place_dao.get(place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.get("/search/", response_model=List[PlaceRead])
def search_and_save_places(query: str, db: Session = Depends(get_db)):
    data = search_places(query)
    places = extract_places(data)
    place_dao = PlaceDAO(db)
    for place_data in places:
        place_dao.create(PlaceCreate(**place_data))
    return place_dao.get_all()
