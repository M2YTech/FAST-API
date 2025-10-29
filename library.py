from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
import json, os

app = FastAPI()

clients = []
notifications = []

class BookUpdate(BaseModel):
    title : str | None = None
    author : str | None = None

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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)

async def send_notification(message: str):
    notifications.append(message)
    for client in clients:
        await client.send_text(message)

@app.get("/")
def index():
    return {"Hello world"}

@app.get("/notifications")
def get_notifications():
    return {"notifications": notifications}


@app.get("/get_data/{book_id}")
def display_data(book_id: int):
    detail = view_books()
    for details in detail:
        if details["id"] == book_id:
            return {"id": details["id"], "title": details["title"], "author": details["author"]}

@app.post("/add_books/add_book")
async def add_book(title: str, author: str):
    data = view_books()
    new_id = len(data) + 1
    book = {"id": new_id, "title": title, "author": author}
    data.append(book)
    save_data(data)
    await send_notification(f"New book added: {title} by {author}")
    return book

@app.put("/update-data/{book_id}")
async def modify_books(book_id: int, book_update : BookUpdate):
    data = view_books()
    found = False

    for book in data:
        if book["id"] == book_id:
            if book_update.title:
                book["title"] = book_update.title
            if book_update.author:
                book["author"] = book_update.author
            found = True
            break
    if not found:
        return {"error": f"Book with ID {book_id} not found."}
    
    save_data(data)
    await send_notification(f"Book with ID {book_id} has been updated.")
    return {"message": "Book updated successfully", "book": book}

@app.delete("/delete-books/{book_id}")
async def delete_book(book_id: int):
    data = view_books()
    
    data = [book for book in data if book["id"] != book_id]

    for index, book in enumerate(data, start=1):
        book["id"] = index
    
    save_data(data)
    await send_notification(f"Book with ID {book_id} deleted successfully.")
    return {"message": "Book deleted successfully"}