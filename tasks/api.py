from typing import Annotated
from fastapi import APIRouter, Body, Response, status
from starlette.requests import Request
#from starlette.templating import Jinja2Templates
from . import models, schemas

#templates = Jinja2Templates(directory="templates")

task_router = APIRouter(prefix="/tasks",
                        tags=["tasks"])

@task_router.get("/hi")
def hello():
    return "hi"

@task_router.get("/all")
async def all_tasks():
    tasks = await models.Task.objects.all()
    return tasks
# @task_router.get("/tasks")
# async def list_tasks():
#     tasks = await models.Task.objects.all()
#     return {"tasks": tasks}


# @task_router.post("/task")
# async def create_task(task: Annotated[
#                       models.Task,
#                       Body(
#                     examples=[
#                             {
#                                 "name": "написать сервис",
#                                 "description": "а он должен делать то...",
#                                 "author": "id автора",
#                             }
#                         ],
#                     )]):
    
#     print(task)
#     return await task.save()
    
