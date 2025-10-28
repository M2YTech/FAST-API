import json,os

library_database = "library.json"

def view_books():
    if os.path.exists(library_database):
        with open(library_database, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return [] 

def save_data(data):
    with open(library_database, "w") as f:
        json.dump(data, f, indent=2)


def add_books(title, author):
    data = view_books()
    new_id = len(data) + 1
    book = {"id": new_id, "title": title, "author": author}
    data.append(book)
    save_data(data)
    return book

def update_book(book_id, title= None, author=None):
    data = view_books()
    found = False

    for book in data:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            found = True
            break
    if not found:
        return {"error": f"Book with ID {book_id} not found."}
    
    save_data(data)
    return {"message": "Book updated successfully", "book": book}

def delete_book(book_id):
    data = view_books()
    data = [ book for book in data if book["id"] != book_id]

    for index, book in enumerate(data, start=1):
        book["id"] = index

    save_data(data)
    return {"message": "Book deleted successfully"}
    
def fetch_book(book_id):
    data = view_books()
    for book in data:
        if book["id"] == book_id:
            return {"id": book["id"], "title": book["title"], "author": book["author"]}


print(fetch_book(2))
# print(view_books())
# print(add_books("key to sucess", "brian tracy"))
# print(update_book(2, author="james"))
# print(delete_book(2))

