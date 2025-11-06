import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def get_books_by_author(author_name):
    return list(Book.objects.filter(author__name=author_name))


def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return list(library.books.all())
    except Library.DoesNotExist:
        return []


def get_librarian_for_library(library_name):
    try:
        return Librarian.objects.get(library__name=library_name)
    except Librarian.DoesNotExist:
        return None


if __name__ == "__main__":
    print("Books by George Orwell:", [b.title for b in get_books_by_author("George Orwell")])
    print("Books in 'Central Library':", [b.title for b in get_books_in_library("Central Library")])
    librarian = get_librarian_for_library("Central Library")
    print("Librarian:", librarian.name if librarian else "None")