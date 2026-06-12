import datetime
from sqlmodel import Field, SQLModel, create_engine


# 创建模型 -> 表
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(default="admin", max_length=10)
    password: str = Field(default="123456", max_length=10)
    created_time: str = Field(default=datetime.datetime.now())


MYSQL_NAME = "user"
MYSQL_URL = f"mysql+pymysql://root:123456@localhost:3306/{MYSQL_NAME}"
# 创建引擎
engine = create_engine(MYSQL_URL)

def create_table():
    SQLModel.metadata.create_all(engine)