import json
import os

file_name = "library.json"

if os.path.exists(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
else:
    data = []

title = input("Enter name of the Book: ")
author = input("Enter name of the author: ")
new_data = {"id": len(data)+1, "title": title, "author": author}

data.append(new_data)

with open(file_name, "w") as f:
    json.dump(data, f, indent=2)

print("Successfully added the book")

