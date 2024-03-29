from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from database import users









class User(users.Model, UserMixin):
    __tablename__ = "users"
    id = users.Column(users.Integer, primary_key=True,autoincrement=True)
    email = users.Column(users.String(250), nullable=False, unique=True)
    username = users.Column(users.String(250), nullable=True, unique=True)
    clippings_filename = users.Column(users.String(250), nullable=True)
    confirmed = users.Column(users.String(10),nullable=True)
    password = users.Column(users.String(1000), nullable=True)
    first_name = users.Column(users.String(250), nullable=True)
    last_name = users.Column(users.String(250), nullable=True)
    continent = users.Column(users.String(250), nullable=True)
    user_photo = users.Column(users.String(250),nullable=True)
    posts = relationship("Posts", back_populates="user")
    books = relationship("Books",back_populates="highlight_owner")


class Posts(users.Model):
    __tablename__ = "posts"
    id = users.Column(users.Integer, primary_key=True, nullable=True,autoincrement=True)
    author_id = users.Column(users.String, users.ForeignKey('users.id'), nullable=True)
    quote_author = users.Column(users.String,nullable=True)
    user = relationship("User", back_populates="posts")
    body = users.Column(users.Text, nullable=True)
    quote = users.Column(users.String(250))
    date = users.Column(users.String(250), nullable=True)
    user_quote = users.Column(users.String(250), nullable=False)
    photo = users.Column(users.String(500), nullable=True)


class Books(users.Model):
    __tablename__ = "highlights"
    id = users.Column(users.Integer, primary_key=True, nullable=True, autoincrement=True)
    highlight_id = users.Column(users.String, users.ForeignKey('users.id'), nullable=True)
    highlight_owner = relationship("User",back_populates="books")
    original_quote = users.Column(users.String,nullable=False)
    writer_quote = users.Column(users.String,nullable=False)
    date_added = users.Column(users.String,nullable=True)
    paper = users.Column(users.Boolean)





