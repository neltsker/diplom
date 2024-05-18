from pydantic import BaseModel


class Task(BaseModel):
    id: int
    author: int
    name: str
    descripion: str


class TaskCreate(Task):
    author: int
    name: str
    descripion: str
