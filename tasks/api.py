from typing import Annotated
from fastapi import APIRouter
from . import schemas
from models.models import *

from fastui import FastUI, AnyComponent, components as c
from fastui.components.display import DisplayLookup
from fastui.events import GoToEvent, BackEvent, PageEvent
from fastui.forms import fastui_form

task_router = APIRouter(prefix="/api",
                        tags=["tasks"])


@task_router.get("/task/all", response_model=FastUI, response_model_exclude_none=True)
async def all_tasks():
    tasks = await Task.objects.all()
    if tasks == []:
            return [
            c.Page(
                components=[
                    c.Heading(text="Досок нет", level=2),
                    c.Div(components=[
                    c.Text(text="Для создания новой доски нажмите кнопку")
                ]),
                c.Div(components=[
                    c.Button(text="Новая задача", on_click=GoToEvent(url='/task/new'))
                ])
                    
                ]
            )]
    return [
            c.Page(
                components=[
                    c.Heading(text="Список задач", level=2),
                    c.Table(
                        data=tasks,
                        columns=[
                            DisplayLookup(field='name', on_click=GoToEvent(url='/task/{id}/')),
                            DisplayLookup(field='id')
                        ]
                    ),
                ]
            )]



@task_router.get("/desk/all", response_model=FastUI, response_model_exclude_none=True)
async def all_desk( ):
    desks = await Desk.objects.all()
    if desks == []:
        return [
        c.Page(
            components=[
                c.Heading(text="Досок нет", level=2),
                  c.Div(components=[
                 c.Text(text="Для создания новой доски нажмите кнопку")
            ]),
            c.Div(components=[
                 c.Button(text="Новая доска", on_click=GoToEvent(url='/desk/new'))
            ])
                
            ]
        )]
    return [
        c.Page(
            components=[
                c.Heading(text="Список досок", level=2),
                 c.Table(
                    data=desks,
                    columns=[
                        DisplayLookup(field='name', on_click=GoToEvent(url='/desk/{id}/')),
                        DisplayLookup(field='id')
                    ]
                ),
            ]
        )]


@task_router.post("/task", response_model=FastUI, response_model_exclude_none=True)
async def task_new(form: Annotated[schemas.TaskCreate, fastui_form(schemas.TaskCreate)]):
    try:
        task = await Task.objects.create(name=form.name, description=form.description, type = form.type)
        task.save
        desk = await Desk.objects.get(id=form.desk)
        if desk.tasks == None:
            desk.tasks = []
            desk.save
        desk.tasks.append(task.id)
        desk.save
        return c.FireEvent(event=GoToEvent(url='/task/{task.id}'))
    except Exception as e:
        return [ c.Toast(
                    title='Toast',
                    body=[c.Paragraph(text='This is a toast.')],
                    open_trigger=PageEvent(name='show-toast'),
                    position='bottom-end',
                ),]


@task_router.post("/desk", response_model=FastUI, response_model_exclude_none=True)
async def desk_new(form: Annotated[schemas.DeskCreate, fastui_form(schemas.DeskCreate)]):
    try:
        desk = await Desk.objects.create(name=form.name, description=form.description)
        desk.save
        return c.FireEvent(event=GoToEvent(url='/desk/{desk.id}'))
    except Exception as e:
        return [ c.Toast(
                    title='Toast',
                    body=[c.Paragraph(text='This is a toast.')],
                    open_trigger=PageEvent(name='show-toast'),
                    position='bottom-end',
                ),]


@task_router.get("/task/{task_id}/", response_model=FastUI, response_model_exclude_none=True)
async def task_view(task_id: int) -> list[AnyComponent]:
    task = await Task.objects.get(id = task_id)
    return [
        c.Page(
            components=[
                c.Heading(text="task one view", level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=task),
            ]
        ),
    ]


@task_router.get("/desk/{desk_id}/", response_model=FastUI, response_model_exclude_none=True)
async def desk_view(desk_id: int) -> list[AnyComponent]:
    desk = await Desk.objects.get(id = desk_id)
    if desk.tasks != None:
        tasks_data = c.Table(
                    data=desk.tasks,
                    columns=[
                        DisplayLookup(field='name', on_click=GoToEvent(url='/task/{id}/')),
                        DisplayLookup(field='id')
                    ]
                )
    else:
        tasks_data = c.Button(text="Новая задача", on_click=GoToEvent(url='/task/new'))
    return [
        c.Page(
            components=[
                c.Heading(text="Desk one view", level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=desk),
                tasks_data
            ]
        ),
    ]

@task_router.get("/desk/new", response_model=FastUI, response_model_exclude_none=True)
def new_desk() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(text="hi", level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.ModelForm(
                    type= "ModelForm",
                    model = schemas.DeskCreate,
                    submit_url= "/api/desk",
                    method = 'POST',
                    display_mode ="page"
                )
            ]
        ),
    ]

@task_router.get("/task/new", response_model=FastUI, response_model_exclude_none=True)
def new_task() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(text="task create form", level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.ModelForm(
                    type= "ModelForm",
                    model = schemas.TaskCreate,
                    submit_url= "/api/task",
                    method = 'POST',
                    display_mode ="page"
                )
            ]
        ),
    ]

