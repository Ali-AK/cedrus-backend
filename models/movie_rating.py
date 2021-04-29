from sqlalchemy import Column, Integer, ForeignKey

from database import Base, session
from .user import User


class MovieRating(Base):
    __tablename__ = 'movies_rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer)

    def get_user_by_id(self):
        user = session.query(User).filter(User.id == self.user_id).first()
        return user.username

    # def get_movie_by_id(self):
    #     movie = session.query(Movie).filter(Movie.id == self.movie_id).first()
    #     return movie.title
