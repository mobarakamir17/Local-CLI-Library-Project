import os
import time
import sys
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db_connector import init_db, SessionLocal, Base
from book import Book
from author import Author
from genre import Genre
from book_data import book_data

# Color definitions
white = "\033[1;37;49m"
red = "\033[1;31;49m"
yellow = "\033[1;33;49m"
green = "\033[1;32;49m"
magenta = "\033[1;35;49m"
cyan = "\033[1;36;49m"

# Database setup
engine = create_engine('sqlite:///lib/db/books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    init_db()

    # Display animations from book.txt and reading.txt
    display_animations(["lib/book.txt", "lib/reading.txt"], delay=0.4)

    # Display welcome message with typewriter effect
    welcome_message = (
        f"\n\n\t\t\t\t\t\t\t\t {green}Welcome to the library!\n\n"
    )

    
    # # Create a new session
    session = SessionLocal()
    
    try:
        for book_info in book_data:
            author = Author(name=book_info["author"])
            genre = Genre(name=book_info["genre"])
            book = Book(
                title=book_info["title"],
                author=author,
                genre=genre,
                published_date=book_info["published_date"],
                description=book_info["description"]
            )
            session.add_all([author, genre, book])

        session.commit()
        click.echo("Book data added successfully.")

        
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


def display_animations(filenames, delay=1, repeat=4):
    frames = []
    for name in filenames:
        with open(name, 'r', encoding='utf8') as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(''.join(frame))
            time.sleep(delay)
            os.system('clear')
    
if __name__ == "__main__":
    main()