import json
from book import Book

class Library:
    def __init__(self,data_file="library.json"):
        self.data_file = data_file
        self.books = []
        self.load_books()

    def load_books(self,data_file ="library.json"):
        try:
            with open(self.data_file,"r",encoding="utf-8") as f:
                book_data = json.load(f)
                self.books = [Book(**data) for data in book_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self, data_file="library.json"):
        book_data = [data.__dict__ for data in self.books]
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(book_data, f, indent=4)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def add_book(self, book):
        if not self.find_book(book.isbn):
            self.books.append(book)
            self.save_books()
            return True
        return False

    def remove_book(self, isbn):
        book_to_remove = self.find_book(isbn)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            return True
        return False

    def list_books(self):
        if not self.books:
            print("There are no added books.")
        else:
            for book in self.books:
                print(book)