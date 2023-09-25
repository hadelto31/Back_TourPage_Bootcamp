from sqlalchemy import Column, Integer, String, Float

from db.db_connection import Base


class CardTravelModel(Base):
    __tablename__ = 'cards_travels'

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    city = Column(String)
    rate = Column(Float)
    price = Column(Float)
    image_url = Column(String)
