from fastapi import FastAPI
import json


app = FastAPI()

file = "books.json"

def read_file():
    with open(file, "r") as f:
        return json.load(f)

def write_file():
    with open(file, "w") as f:
        json.dump(data, f)

@app.get("/")
def index():
    return "Hello World"

@app.get("/fetched-update/{book_id}")
def get_book(book_id: str):
    books = read_file()
    if book_id not in books:
        return {"Error": "Book not Found"}
    return books[book_id]
    
@app.post("/add-book/{book_id}")
def create_Book(book_id: int):
    books = write_file()
    if book_id in books:
        return {"Error": "Book Already Exist"}
    books[book_id] = books
    return books[book_id]
