from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
    }
]


# 获取所以数据信息
@app.get("/books")
async def get_books() -> list[dict]:
    return books


# 获取指定书籍信息
@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# 更新书籍信息
class BookUpdate(BaseModel):
    title: str
    author: str
    year: int


@app.put("/books/{book_id}")
async def update_book(book_id: int, book_update: BookUpdate) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["year"] = book_update.year
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# 创建新的书籍信息
class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    year: int


@app.post("/books")
async def create_book(book_create: BookCreate) -> dict:
    new_book = book_create.model_dump()
    print(new_book)
    books.append(new_book)
    return new_book


# 删除书籍信息
@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": f"Book{book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")