import pytest
import os
from library import Library
from book import Book

@pytest.fixture
def library():
    test_file = 'test_library.json'
    if os.path.exists(test_file):
        os.remove(test_file)
    lib = Library(data_file=test_file)
    yield lib
    os.remove(test_file)

def test_add_book(library):
    book = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    assert library.add_book(book) is True
    assert len(library.books) == 1
    assert library.books[0].title == "The Hobbit"

def test_add_existing_book(library):
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "123456789")
    library.add_book(book1)
    assert library.add_book(book2) is False
    assert len(library.books) == 1

def test_remove_book(library):
    book = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    library.add_book(book)
    assert library.remove_book("123456789") is True
    assert len(library.books) == 0

def test_remove_nonexistent_book(library):
    book = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    library.add_book(book)
    assert library.remove_book("999999999") is False
    assert len(library.books) == 1

def test_find_book(library):
    book = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    library.add_book(book)
    found_book = library.find_book("123456789")
    assert found_book is not None
    assert found_book.title == "The Hobbit"

def test_save_and_load(library):
    book = Book("The Hobbit", "J.R.R. Tolkien", "123456789")
    library.add_book(book)
    new_library = Library(data_file='test_library.json')
    assert len(new_library.books) == 1
    assert new_library.books[0].title == "The Hobbit"

def test_add_book_by_isbn_success(library):
    isbn = "978-0743273565"
    result = library.add_book_by_isbn(isbn)
    assert "is added" in result
    assert len(library.books) == 1
    assert library.books[0].title == "The Great Gatsby"

def test_add_book_by_isbn_duplicate(library):
    isbn = "978-0743273565"
    library.add_book_by_isbn(isbn)
    result = library.add_book_by_isbn(isbn)
    assert "The book is already added" in result
    assert len(library.books) == 1
