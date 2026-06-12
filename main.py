from contextlib import asynccontextmanager

from fastapi import FastAPI, Path, Query, Depends
from pydantic import BaseModel, Field

from db.create_table import create_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    try:
        create_table()
        print("模型加载成功")
    except Exception as e:
        print(e)
        print("模型加载失败")
    yield
    # Clean up the ML models and release the resources



app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/hello")
def read_hello():
    return {"msg": "我正在学习 fastapi"}


# 路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# 路径参数Path()类型注解
@app.get("/books/{id}")
def get_book(id: int = Path(..., gt=0, lt=100, description="id must be greater than 0 <100")):
    return {"id": id}


@app.get("/books/{name}")
def get_book_name(name: str = Path(..., min_length=2, max_length=10)):
    return {"name": name}


# 查询参数+注解
@app.get("/books/query/")
def get_book(q: str = Query(..., min_length=2, max_length=10)):
    return {"q": q}


# 请求体参数
# 注解
class User(BaseModel):
    username: str = Field(default='admin', min_length=2, max_length=10,
                          description="username must be greater than 2 and less than 10")
    password: str = Field(default='123456', min_length=6, max_length=10,
                          description="password must be greater than 6 and less than 10")


# 中间件
@app.middleware("http")
async def my_middleware(request, call_next):
    print("中间件开始")
    response = await call_next(request)
    print("中间件结束")
    return response

# 依赖注入
async def common_parameters(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=50),
):
    return {"skip":skip,"limit": limit}

@app.get("/news/news_list")
async def news_list(commons: dict = Depends(common_parameters)):
    return commons