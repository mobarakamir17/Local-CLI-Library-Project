import click
import os
from db.models import SessionLocal, Book, Author, Genre
from main import main as run_main, display_animations, book_pic, reading
from functions import menu

if __name__ == '__main__':
    print("Loading the Library...")
    display_animations(book_pic,delay=0.4)
    menu()

