from sqlalchemy import Column, Integer, ForeignKey

from database import Base, session
from .user import User
from .movie import Movie


class MovieRating(Base):
    __tablename__ = 'movies_rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))

    def get_user_by_id(self):
        return session.query(User).filter_by(User.id == self.user_id).first()

    def get_movie_by_id(self):
        return session.query(Movie).filter_by(User.id == self.movie_id).first()