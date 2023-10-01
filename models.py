from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    '''User model'''
    
    __table_name__ = 'user'
    
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    username = sa.Column(sa.String, unique=True, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    
    todos = relationship('Todo', back_populates='todo_owner')
    
    
class Todo(db.Model):
    '''Todo Model'''
    
    __table_name__ = 'todo'
    
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    todo_name = sa.Column(sa.String, nullable=False)
    priority = sa.Column(sa.String, nullable=False)
    completion_date = sa.Column(sa.String, nullable=False)
    completion_time = sa.Column(sa.String, nullable=False)
    is_complete = sa.Column(sa.Boolean, nullable=True, default=False)
    
    owner_id = sa.Column(sa.Integer, sa.ForeignKey(column='user.id', ondelete='CASCADE'), nullable=False)
    todo_owner = relationship('User', back_populates='todos')