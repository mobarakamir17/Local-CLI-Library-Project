import click
import os
from db.models import SessionLocal, Book, Author, Genre
from main import main as run_main, display_animations, book_pic, reading
from functions import menu



# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def main():
    
#     run_main()

if __name__ == '__main__':
    # display_animations(book_pic,delay=0.4)
    run_main()
    menu()

# display_animations(book_pic, delay=0.4)

# @click.group()
# def cli():
#     pass

# @cli.command()
# def list_books():
#     """List all books in the library."""
#     session = SessionLocal()
#     books = session.query(Book).all()
#     for book in books:
#         click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
#     session.close()

# @cli.command()
# @click.argument('author_name')
# def search_by_author(author_name):
#     """Search books by author."""
#     session = SessionLocal()
#     books = session.query(Book).join(Author).filter(Author.name.ilike(f"%{author_name}%")).all()
#     if books:
#         for book in books:
#             click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
#     else:
#         click.echo(f"No books found by author {author_name}")
#     session.close()

# @cli.command()
# @click.argument('book_title')
# def search_by_title(book_title):
#     """Search books by title."""
#     session = SessionLocal()
#     books = session.query(Book).filter(Book.title.ilike(f"%{book_title}%")).all()
#     if books:
#         for book in books:
#             click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
#     else:
#         click.echo(f"No books found with title {book_title}")
#     session.close()

# @cli.command()
# @click.argument('genre')
# def filter_by_genre(genre):
#     """Filter books by genre."""
#     session = SessionLocal()
#     books = session.query(Book).join(Genre).filter(Genre.name.ilike(f"%{genre}%")).all()
#     if books:
#         for book in books:
#             click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
#     else:
#         click.echo(f"No books found in genre {genre}")
#     session.close()

# @cli.command()
# def add_book():
#     """Add a new book to the library."""
#     session = SessionLocal()
#     new_book = {
#         "title": click.prompt("Enter the title: "),
#         "author": click.prompt("Enter the author: "),
#         "genre": click.prompt("Enter the genre: "),
#         "published date": click.prompt("Enter the published date"),
#         "description": click.prompt("Enter a short description here")
#     }
#     # Create new Book, Author, Genre objects and add them to the session
#     # Commit changes
#     session.close()


# if __name__ == '__main__':
#     cli()
