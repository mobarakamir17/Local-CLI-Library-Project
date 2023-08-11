from db.models import SessionLocal, Book, Author, Genre
from main import main as display_animations, reading

def menu():

    print("Select an option from the menu below:")
    selection = input("1. List Books    2. Add Book     3. Filter   4. Leave Library\n")
    if selection == "1":
        list_books()
    elif selection == "2":
        add_book()
    elif selection == "3":
        print("Select your filter type:")
        filter_selection = input("1. Author 2. Genre\n")
        if filter_selection == "1":
           search_by_author_menu()
        elif filter_selection == "2":
            filter_by_genre()
    elif selection == "4":
        display_animations(reading, delay=1)
        print("Goodbye!")
        exit()

def list_books():
    """List all books in the library."""
    session = SessionLocal()
    books = session.query(Book).all()
    genres = session.query(Genre).all()
    authors = session.query(Author).all()

    for book in books:
        book_author = next((author for author in authors if author.book_id == book.id), None)
        book_genre = next((genre for genre in genres if genre.book_id == book.id), None)
        if book_author:
            print(f"{book.title} by {book_author.name} ({book_genre.name})")
    session.close()
    menu()

def search_by_author_menu():
    """Search books by author."""
    author_name = input("Enter the author's name: ")
    session = SessionLocal()
    books = session.query(Book).join(Author).filter(Author.name.ilike(f"%{author_name}%")).all()
    if books:
        for book in books:
            author_names = ", ".join([author.name for author in book.author])
            genre_names = ", ".join([genre.name for genre in book.genre])
            print(f"{book.title} by {author_names} ({genre_names})")
    else:
        print(f"No books found by author {author_name}")

    session.close()
    menu()

def filter_by_genre():
    """Filter books by genre."""
    session = SessionLocal()
    genre_input = input("Enter the genre to filter by: ")
    books = session.query(Book).join(Genre).filter(Genre.name.ilike(f"%{genre_input}%")).all()

    if books:
        for book in books:
            author_name = book.author[0].name if book.author else "Unknown"
            genre_names = ", ".join([genre.name for genre in book.genre])
            print(f"{book.title} by {author_name} ({genre_names})")
    else:
        print(f"No books found in library with the genre: {genre_input}")

    session.close()
    menu()

def add_book():
    """Add a new book to the library."""
    session = SessionLocal()
    new_book = {
        "title": input("Enter the title: "),
        "author": input("Enter the author: "),
        "genre": input("Enter the genre: "),
        "published_date": input("Enter the published date: "),
        "description": input("Enter a short description here: ")
    }
    # Create new Book, Author, Genre objects and add them to the session
    add_book = Book(title=new_book["title"], published_date=new_book["published_date"], description=new_book["description"])
    session.add(add_book)
    session.commit()
    add_genre = Genre(name=new_book["genre"], book_id=add_book.id)
    add_author = Author(name=new_book["author"], book_id=add_book.id)

    session.add(add_genre)
    session.add(add_author)

    session.commit()
    # Commit changes
    session.close()
    menu()
