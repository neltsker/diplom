from pydantic import BaseModel, Field


class DeskCreate(BaseModel):
    name : str = Field(title="Название")
    description : str = Field(title = "Описание")
    
class TaskCreate(BaseModel):
    name : str =Field(title="Название")
    description : str =Field(title = "Описание")
    type: str = Field(title = "Тип")
    desk: int = Field(title = "id доски задач")
