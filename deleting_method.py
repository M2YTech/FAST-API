import json

file_name = "library.json"

with open(file_name, "r") as f:
    data = json.load(f)

book_id = int(input("Enter the Id of the book: "))

data = [ book for book in data if book["id"] != book_id]


for index, book in enumerate(data, start=1):
    book["id"] = index

with open(file_name, "w") as f:
    json.dump(data, f, indent=2)

print("Successfully deleted the file")