from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UnicodeText,
)

Base = declarative_base()


class DbAbsLayer(object):
    # Database Abstraction Layer
    def __init__(self):
        self.engine = create_engine('sqlite:///neuro.db')
        # create any tables that don't yet exist
        Base.metadata.create_all(self.engine)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self

    def clear_db(self):
        # drop all tables
        Base.metadata.drop_all(self.engine)
        # create tables to maintain schema
        Base.metadata.create_all(self.engine)


class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lyrics = Column(UnicodeText(64))
    artist_id = Column(Integer, ForeignKey('artists.id'))


class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
