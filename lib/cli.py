import click
from lib.db.db_connector import init_db, SessionLocal
from lib.db.models.book import Book, Author, Genre

@click.group()
def cli():
    pass

@cli.command()
def list_books():
    """List all books in the library."""
    session = SessionLocal()
    books = session.query(Book).all()
    for book in books:
        click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
    session.close()

@cli.command()
@click.argument('author_name')
def search_by_author(author_name):
    """Search books by author."""
    session = SessionLocal()
    books = session.query(Book).join(Author).filter(Author.name.ilike(f"%{author_name}%")).all()
    if books:
        for book in books:
            click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
    else:
        click.echo(f"No books found by author {author_name}")
    session.close()

@cli.command()
@click.argument('book_title')
def search_by_title(book_title):
    """Search books by title."""
    session = SessionLocal()
    books = session.query(Book).filter(Book.title.ilike(f"%{book_title}%")).all()
    if books:
        for book in books:
            click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
    else:
        click.echo(f"No books found with title {book_title}")
    session.close()

@cli.command()
@click.argument('genre')
def filter_by_genre(genre):
    """Filter books by genre."""
    session = SessionLocal()
    books = session.query(Book).join(Genre).filter(Genre.name.ilike(f"%{genre}%")).all()
    if books:
        for book in books:
            click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")
    else:
        click.echo(f"No books found in genre {genre}")
    session.close()

if __name__ == '__main__':
    cli()
