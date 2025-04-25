from sqlalchemy import Column, Integer, String, Float
from app.dao.database import Base

class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    category = Column(String)
    rating = Column(Float, default=0.0)
    description = Column(String, nullable=True)
