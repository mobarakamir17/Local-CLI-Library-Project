import os
import time
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import SessionLocal, Base, Book, Author, Genre
from book_data import book_data


# Color definitions
white = "\033[1;37;49m"
red = "\033[1;31;49m"
yellow = "\033[1;33;49m"
green = "\033[1;32;49m"
magenta = "\033[1;35;49m"
cyan = "\033[1;36;49m"

# Database setup
engine = create_engine('sqlite:///db/books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

book_pic = ["book.txt","book2.txt","book3.txt","book.txt"]
reading = ["reading.txt","reading2.txt"]

def main():

    
    # Create a new session
    session = SessionLocal()

    try:
        # Loop through book_data and create books
        book_list = []
        for book_info in book_data:
            book = Book(
                title=book_info["title"],
                # author=author,
                # genre=genre,
                published_date=book_info["published_date"],
                description=book_info["description"]
            )
            session.add(book)
            book_list.append(book)
        session.commit()

        for book_info in book_data:
            book = next((book for book in book_list if book.title == book_info["title"]), None)
            author = Author(
                name=book_info["author"],
                book_id=book.id)
            session.add(author) 
            genre = Genre(
                name=book_info["genre"],
                book_id=book.id)
            session.add(genre)
        # Commit changes to the database
        session.commit()

    except Exception as e:
        session.rollback()
        print("An error occurred:", e)

    finally:
        # Close the session
        session.close()

def typewriter(message, delay=0.02):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def display_animations(filenames, delay=1, repeat=3):
    frames = []
    for name in filenames:
        with open(name, 'r', encoding = 'utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(''.join(frame))
            time.sleep(delay)
            os.system('clear')
    
if __name__ == "__main__":
    main()