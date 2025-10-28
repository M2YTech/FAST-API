import json

file_name = "library.json"

with open(file_name, "r") as f:
    data = json.load(f)

book_id = int(input("Enter the Id of the book: "))
new_title = input("Enter the new title here: ")

for book in data:
    if book["id"] == book_id:
        book["title"] = new_title
        break


with open(file_name, "w") as f:
    json.dump(data, f, indent=2)

print("Successfully updated the file")