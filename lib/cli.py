import click
from db.db_connector import SessionLocal
from book import Book, Author, Genre
from book_data import book_data
from library import load_animation


@click.group()
def cli():
    pass

@cli.command()
def open_library():
    """Populate the database with book data and start the animation."""
    # Start the animation
    load_animation(["lib/book.txt", "lib/reading.txt"], delay=0.4)

    # Create a new session
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
        click.echo("Library opened and populated with book data.")

    except Exception as e:
        session.rollback()
        print("An error occurred:", e)

    finally:
        # Close the session
        session.close()

if __name__ == '__main__':
    cli()
