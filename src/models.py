import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()


def setup_db(app):
    '''
    setup_db(app)
    | binds a flask application and a SQAlchemy service
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Actor(db.Model):
    __tablename__ = 'Actor'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer(), nullable=False)
    gender = Column(String(50), nullable=False)

    def __init__(name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    __tablename__ = 'Movie'
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    year = Column(Integer(), nullable=False)
    month = Column(Integer())
    day = Column(Integer())
    genre = Column(String(50), nullable=False)

    def __init__(title, year, month, day, genre):
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.genre = genre

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'genre': self.genre
        }
