import os
import uvicorn
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from book import Book
from library import Library

class BookModel(BaseModel):
    title: str
    author: str
    isbn: str


class IsbnRequest(BaseModel):
    isbn: str

app = FastAPI(
    title="Library API",
    description="A simple library management API developed with Python.",
    version="1.0.0"
)

library = Library()


@app.get("/books", response_model=List[BookModel])
def get_all_books():
    return library.books


@app.post("/books", response_model=BookModel)
def add_book_with_isbn(request: IsbnRequest):
    if library.find_book(request.isbn):
        raise HTTPException(status_code=409, detail="A book with this ISBN already exists.")

    try:
        url = f"https://openlibrary.org/isbn/{request.isbn}.json"
        response = httpx.get(url, follow_redirects=True)

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="No book was found for the given ISBN.")

        response.raise_for_status()
        book_data = response.json()

        title = book_data.get("title", "Unknown")

        authors_list = []
        for author in book_data.get("authors", []):
            if isinstance(author, dict) and 'name' in author:
                authors_list.append(author.get('name', 'Unknown'))
            elif isinstance(author, str):
                authors_list.append(author)

        author_str = ", ".join(authors_list) or "Unknown"

        new_book = Book(title=title, author=author_str, isbn=request.isbn)
        library.add_book(new_book)

        return new_book

    except httpx.HTTPStatusError:
        raise HTTPException(status_code=response.status_code,
                            detail=f"An error was returned from the API: {response.text}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Connection error: The API could not be reached. Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@app.delete("/books/{isbn}")
def remove_book_by_isbn(isbn: str):
    if library.remove_book(isbn):
        return {"message": f"Book with ISBN {isbn} was successfully deleted."}
    else:
        raise HTTPException(status_code=404, detail=f"Book with ISBN {isbn} was not found.")


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)