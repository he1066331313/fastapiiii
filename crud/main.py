from fastapi import FastAPI, HTTPException
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


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None


# 获取所有数据信息
@app.get("/books", response_model=list[Book])
async def get_books():
    return books


# 获取指定书籍信息
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


# 更新书籍信息（部分更新）
@app.patch("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    update_data = book_update.model_dump(exclude_unset=True)
    book.update(update_data)
    return book


# 创建新的书籍信息
@app.post("/books", response_model=Book, status_code=201)
async def create_book(book_create: BookCreate):
    new_id = max(b["id"] for b in books) + 1 if books else 1
    new_book = {"id": new_id, **book_create.model_dump()}
    books.append(new_book)
    return new_book


# 删除书籍信息
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    books.remove(book)
    return {"message": f"Book {book_id} deleted"}
