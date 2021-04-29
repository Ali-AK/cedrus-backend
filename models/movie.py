from database import Base, session
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .genre import Genre
from .movie_rating import MovieRating


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"))

    movie_rating = relationship("MovieRating")

    def get_genre_by_id(self):
        genre = session.query(Genre).filter(Genre.id == self.genre_id).first()
        return genre.name

    def get_rating_by_id(self):
        rating = session.query(MovieRating).filter(MovieRating.movie_id == self.id).first()
        if rating is None:
            return 0
        return rating.rating
