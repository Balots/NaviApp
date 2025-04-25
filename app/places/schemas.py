from pydantic import BaseModel

class PlaceCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    category: str
    rating: float = 0.0
    description: str = None

class PlaceRead(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float
    category: str
    rating: float
    description: str = None

    class Config:
        orm_mode = True
