from fastapi import FastAPI,Path

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/hello")
def read_hello():
    return {"msg":"我正在学习 fastapi"}

# 路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 路径参数Path()类型注解
@app.get("/books/{id}")
def get_book(id: int=Path(...,gt=0,lt=100,description="id must be greater than 0 <100")):
    return {"id":id}

@app.get("/books/{name}")
def get_book_name(name: str=Path(...,min_length=2,max_length=10)):
    return {"name":name}


# 查询参数
@app.get("/books/query/")
def get_book(q: str | None = None):
    return {"q": q}