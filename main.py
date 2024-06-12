from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.events import GoToEvent
from tasks.api import task_router
from auth.api import user_router
import databases
import config

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



app.include_router(task_router)
app.include_router(user_router)


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def hello_world() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                
                 c.Heading(text='Добро пожаловать!', level=2),
            c.Div(components=[
                 c.Text(text="Для перехода к активным доскам нажмите на кнопку ниже")
            ]),
            c.Div(components=[
                 c.Button(text="К доскам", on_click=GoToEvent(url='/desk/all'))
            ])

            ]
        ),
    ]

@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='Home tracker'))
