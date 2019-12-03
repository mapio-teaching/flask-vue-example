from sqlalchemy import Column, Integer, String, Sequence, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'post'

    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    title = Column(String)
    created = Column(DateTime, server_default = func.now())
    body = Column(Text)

    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates = 'posts')

    def __repr__(self):
        return f'<Post: {self.title}>'


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key = True)
    username = Column(String)
    password = Column(String)

    posts = relationship('Post', order_by = Post.id, back_populates = 'user')

    def __repr__(self):
        return f'<User: {self.username}>'
