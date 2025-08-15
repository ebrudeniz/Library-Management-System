class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}. ISBN number is: {self.isbn}"


if __name__ == "__main__":
    book = Book("The Alchemist","Paulo Coelho","123")
    print(book)