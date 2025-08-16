from library import Library
from book import Book

def main():
    library = Library()

    while True:
        print("Library Management System")
        print("1) Add book")
        print("2) Delete book")
        print("3) List all books")
        print("4) Find book")
        print("5) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Book name: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            result = library.add_book_by_isbn(isbn)
            print(result)

        elif choice == 2:
            isbn = input("Enter the ISBN number of book: ")
            if library.remove_book(isbn):
                print("Succesfully deleted.")
            else:
                print("Enter a valid ISBN number.")

        elif choice == 3:
            library.list_books()

        elif choice == 4:
            isbn = input("Enter the ISBN number : ")
            found_book = library.find_book(isbn)
            if found_book:
                print(f"The book found {found_book}.")

        elif choice == 5:
            print("Closing the system!")
            break

        else:
            print("Enter a valid number between 1-5 !")

if __name__ == "__main__":
    main()