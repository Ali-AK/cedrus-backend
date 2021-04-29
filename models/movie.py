from database import Base, session
from sqlalchemy import Column, String, Integer, ForeignKey
from .genre import Genre


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))

    def get_genre_by_id(self):
        genre = session.query(Genre).filter(Genre.id == self.genre_id).first()
        return genre.name
