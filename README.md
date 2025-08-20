# 📚 Library Management System

This project is developed as part of the **Global AI Hub Python 202 Bootcamp**.  
It combines **Object-Oriented Programming (OOP)**, **external API integration**, and **FastAPI** to build a complete library management system in three stages.  

## 🚀 Features
- Add, remove, search, and list books  
- Fetch book details using **ISBN** from the **Open Library API**  
- Persistent data storage with **JSON file**  
- Interactive **command-line menu**  
- REST API built with **FastAPI** (GET, POST, DELETE endpoints)  
- Tested with **pytest**  

---

## 📂 Project Structure
├── book.py # Book class
├── library.py # Library class
├── main.py # CLI application
├── api.py # FastAPI REST API
├── test_library.py # Unit tests with pytest
├── library.json # Persistent data file
├── requirements.txt # Dependencies


## ⚙️ Installation

1. Clone the repository:
   
   git clone https://github.com/ebrudeniz/Library-Management-System.git
   cd library-management

2. Install dependencies:
   
   pip install -r requirements.txt

## 🖥️ Usage

1) Command-Line Application

Run:
    python main.py

Menu options:

1.Add a book (by ISBN)
2.Remove a book
3.List all books
4.Find a book
5.Exit


2) FastAPI REST API

Start the server:
   uvicorn api:app --reload

Open interactive docs: http://127.0.0.1:8000/docs


Endpoints:

GET /books → Get all books
POST /books → Add a book by ISBN
DELETE /books/{isbn} → Remove a book by ISBN

## 🧪 Testing

Run all tests:
pytest


Covers:
Adding and removing books
Handling non-existent books
Searching books
Saving and loading from JSON
Adding books via ISBN (Open Library API)
   
