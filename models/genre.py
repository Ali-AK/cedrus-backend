from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    genres_relation = relationship('Movie')
