"""This module contains all the models used in the application"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# too-few-public-methods ignore because it's a database models here is no methods
Base = declarative_base()

class User(Base):
    """This is the user model"""

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    """This is the post model"""

    def __str__(self):
        return f"Post Content: {self.content}"

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, content={self.content})"

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="posts")


users_data = [
    {"username": "Grigory Lyashchenko", "email": "grigory@example.com", "password": "qwertyqwerty"},
    {"username": "Grigory Perviy", "email": "g1@example.com", "password": "qwertyqwerty"},
    {"username": "Grigory vtoroy", "email": "g2@example.com", "password": "qwertyqwerty"},
]

posts_data = [
    {"title": "First post", "content": "This is post1!", "user_id": 1},
    {"title": "Second post", "content": "This is post2.", "user_id": 2},
    {"title": "Third post", "content": "Hello, post 3!", "user_id": 1},
]
