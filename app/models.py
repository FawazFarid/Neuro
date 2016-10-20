from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Float,
    Text
)

Base = declarative_base()


class DbAbsLayer(object):
    def __init__(self):
        self.engine = create_engine('sqlite:///neuro.db')

    def createSession(self):
        Session = sessionmaker()
        self.session = Session.configure(bind=self.engine)


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lyrics = Column(Text)
    artist_id = Column(Integer, ForeignKey('artists.id'))


class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
