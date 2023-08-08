from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db_connector import Base 

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    books = relationship("Book", back_populates="genre")