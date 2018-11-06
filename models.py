from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# An Artist has many Songs and has many Genres through Songs
# A Genre has many Songs and has many Artists through Songs
# Every Song belongs to an Artist and belongs to a Genre

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    songs = relationship('Song', back_populates='artist') # back populates to the artist property in the song model
    genres = relationship('Genre', secondary='songs', back_populates='artists') # uses the songs join table in order to create a has-many relationship with the Genres class and the artists variable in the Genre class

class Song(Base): # this class will be 'mapped' and used as our join table
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    artist = relationship('Artist', back_populates = 'songs') # this is the artist property in the song model
    genre = relationship('Genre', back_populates = 'songs')
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    songs = relationship('Song', back_populates='genre') #back populates to the genre property in the Song class (because genre has many songs though the Song class)
    artists = relationship('Artist', secondary='songs', back_populates='genres') # back populates to the genres variable in the Artist class


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
