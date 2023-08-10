from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    published_date = Column(Date)
    description = Column(String)

    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="genre")

engine = create_engine('sqlite:///db/books.db')
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()