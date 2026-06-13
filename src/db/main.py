from sqlmodel import create_engine, text, SQLModel
# from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import settings

# 创建引擎,连接数据库
engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True,
)


def init_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM user"))
        for row in result:
            print(f"用户ID: {row[0]}, 用户名: {row[1]}")
