from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(50), nullable=False)
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    user_rating = relationship("MovieRating")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
