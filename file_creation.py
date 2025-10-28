import json

books = [
    {"id": 1, "title": "The Good Book", "author": "james bond"},
    {"id": 2, "title": "The Bad Book", "author": "Lames bond"}
]
file_name = "library.json"
with open(file_name, "w") as f:
    json.dump(books, f, indent=2)

print("Successfully created the file")