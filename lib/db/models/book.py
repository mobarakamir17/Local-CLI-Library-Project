# Define the Book model class here, including its attributes, relationships, and methods for CRUD operations.
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.db_connector import Base 

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