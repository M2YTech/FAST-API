import json
import os 

file_name = "library.json"

with open(file_name, "r") as f:
    data = json.load(f)

for book in data:
    print(f"ID : {book["id"]}, Title: {book["title"]}, Author: {book["author"]}")

def add_book():
    book["id"] = len(book)