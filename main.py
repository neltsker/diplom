from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI

from auth.api import user_router
import databases
import config
from tasks.api import task_router

app = FastAPI()


app.state.database = databases.Database(config.DB_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    yield
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


# @app.on_event("startup")
# async def startup() -> None:
#     database_ = app.state.database
#     if not database_.is_connected:
#         await database_.connect()


# @app.on_event("shutdown")
# async def shutdown() -> None:
#     database_ = app.state.database
#     if database_.is_connected:
#         await database_.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.include_router(task_router)
app.include_router(user_router)
