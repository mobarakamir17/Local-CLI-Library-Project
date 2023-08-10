import os
import time
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db_connector import init_db, SessionLocal, Base
from book import Book
from author import Author
from genre import Genre
# from sqlalchemy.ext.declarative import declarative_base


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

    
    # Create a new session
    session = SessionLocal()
    
    try:
        # Book 1
        author_1 = Author(name="F. Scott Fitzgerald")
        genre_1 = Genre(name="Fiction")
        book_1 = Book(
            title="The Great Gatsby",
            author=author_1,
            genre=genre_1,
            published_date="1925",
            description="The Great Gatsby, F. Scott Fitzgerald’s third book, stands as the supreme..."
        )
        session.add_all([author_1, genre_1, book_1])
        
        # Book 2
        author_2 = Author(name="J.K. Rowling")
        genre_2 = Genre(name="Fantasy Fiction")
        book_2 = Book(
            title="Harry Potter and the Sorcerer’s Stone",
            author=author_2,
            genre=genre_2,
            published_date="1997",
            description="Harry Potter has no idea how famous he is..."
        )
        session.add_all([author_2, genre_2, book_2])

         # Book 3
        author_3 = Author(name="Khaled Hosseini")
        genre_3 = Genre(name="Historical Fiction")
        book_3 = Book(
            title="The Kite Runner",
            author=author_3,
            genre=genre_3,
            published_date="2003",
            description="The unforgettable, heartbreaking story of the unlikely friendship between a wealthy boy and the son of his father’s servant, caught in the tragic sweep of history, The Kite Runner transports readers to Afghanistan at a tense and crucial moment of change and destruction. A powerful story of friendship, it is also about the power of reading, the price of betrayal, and the possibility of redemption; and an exploration of the power of fathers over sons—their love, their sacrifices, their lies."
        )
        session.add_all([author_3, genre_3, book_3])

        # Book 4
        author_4 = Author(name="Edward Powys Mathers")
        genre_4 = Genre(name="Crime Fiction")
        book_4 = Book(
            title="Cain's Jawbone",
            author=author_4,
            genre=genre_4,
            published_date="1934",
            description="Six murders. One hundred pages. Millions of possible combinations… but only one is correct. Can you solve Torquemada’s murder mystery? "
        ) 
        session.add_all([author_4, genre_4, book_4])

        # Book 5
        author_5 = Author(name="Stephen King")
        genre_5 = Genre(name="Horror Fiction")
        book_5 = Book(
            title="The Institute",
            author=author_5,
            genre=genre_5,
            published_date="2019",
            description="In the middle of the night, in a house on a quiet street in suburban Minneapolis, intruders silently murder Luke Ellis’s parents and load him into a black SUV. The operation takes less than two minutes. Luke will wake up at The Institute, in a room that looks just like his own, except there’s no window. And outside his door are other doors, behind which are other kids with special talents—telekinesis and telepathy—who got to this place the same way Luke did: Kalisha, Nick, George, Iris, and ten-year-old Avery Dixon. They are all in Front Half. Others, Luke learns, graduated to Back Half, “like the roach motel,” Kalisha says. 'You check in, but you don’t check out.' In this most sinister of institutions, the director, Mrs. Sigsby, and her staff are ruthlessly dedicated to extracting from these children the force of their extranormal gifts. There are no scruples here. If you go along, you get tokens for the vending machines. If you don’t, punishment is brutal. As each new victim disappears to Back Half, Luke becomes more and more desperate to get out and get help. But no one has ever escaped from the Institute."
        ) 
        session.add_all([author_5, genre_5, book_5])

        # Book 6
        author_6 = Author(name="Russ")
        genre_6 = Genre(name="Biography")
        book_6 = Book(
            title="Its All In Your Head",
            author=author_6,
            genre=genre_6,
            published_date="2019",
            description="In this memoir, Russ inspires readers to walk to their individual rhythms and beat their biggest obstacles: themselves. With chapters named after his most powerful and popular songs, IT'S ALL IN YOUR HEAD will reflect on the lessons he's learned from his career, family, and relationships."
        ) 
        session.add_all([author_6, genre_6, book_6])

        # Book 7 
        author_7 = Author(name="Jordan B. Peterson")
        genre_7 = Genre(name="Self-help Book")
        book_7 = Book(
            title="12 Rules for Life: An Antidote to Chaos",
            author=author_7,
            genre=genre_7,
            published_date="2018",
            description="12 Rules For Life is a story-based, stern yet entertaining self-help manual for young people laying out a set of simple rules to help us become more disciplined, behave better, act with integrity, and balance our lives while enjoying them as much as we can"
        ) 
        session.add_all([author_7, genre_7, book_7])

        # Book 8
        author_8 = Author(name="Robert Kiyosaki")
        genre_8 = Genre(name="Personal Finance")
        book_8 = Book(
            title="Rich dad Poor dad",
            author=author_8,
            genre=genre_8,
            published_date="1997",
            description="Rich Dad Poor Dad is about Robert Kiyosaki and his two dads—his real father (poor dad) and the father of his best friend (rich dad)—and the ways in which both men shaped his thoughts about money and investing. You don't need to earn a high income to be rich. Rich people make money work for them."
        ) 
        session.add_all([author_8, genre_8, book_8])

        # Book 9
        author_9 = Author(name="Mo Gawdat")
        genre_9 = Genre(name="Science and Technology")
        book_9 = Book(
            title="Scary Smart",
            author=author_9,
            genre=genre_9,
            published_date="2021",
            description=" By 2049 AI will be a billion times more intelligent than humans. Scary Smart explains how to fix the current trajectory now, to make sure that the AI of the future can preserve our species. This book offers a blueprint, pointing the way to what we can do to safeguard ourselves, those we love and the planet itself."
        ) 
        session.add_all([author_9, genre_9, book_9])

        # Book 10
        author_10 = Author(name="Patric Radden Keefe")
        genre_10 = Genre(name="True Crime")
        book_10 = Book(
            title="Empire of Pain",
            author=author_10,
            genre=genre_10,
            published_date="2021",
            description="Empire of Pain follows the rise and fall of the elusive Sacklers, the billionaire family behind Purdue Pharma. Its blockbuster drug, OxyContin, was aggressively marketed as safe, but would go on to spur a devastating opioid crisis that claimed hundreds of thousands of lives."
        ) 
        session.add_all([author_10, genre_10, book_10])

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