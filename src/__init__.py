from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.crud.main import router
from src.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    init_db()
    print("连接数据库成功")
    yield
    print("服务关闭")


version = "v1"

app = FastAPI(title="FastAPI-SQLModel", version=version, lifespan=lifespan)

app.include_router(router, prefix=f"/api/{version}")
