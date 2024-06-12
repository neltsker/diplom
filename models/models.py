import ormar
from typing import Optional, List
import config
from auth.models import User
import sqlalchemy
import databases
from typing import ForwardRef

from pydantic import SecretStr


database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()

TaskRef = ForwardRef("Task")

class Task(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database, metadata=metadata
    )

    id : int = ormar.Integer(primary_key=True, autoincrement=True)
    author: Optional[User] = ormar.ForeignKey(User, related_name="author")
    name : str = ormar.String(max_length=100)
    description : str = ormar.Text()
    executor : Optional[User] = ormar.ForeignKey(User, related_name="executor")
    viewers : Optional[List[User]] = ormar.ManyToMany(User, related_name="viewers")
    #another : str = ormar.String(max_length=100)
    type: str = ormar.String(max_length=100)
    related_tasks : TaskRef = ormar.ForeignKey(TaskRef, related_name="related_tasks")


Task.update_forward_refs()

class TaskField(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database, metadata=metadata
    )
    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    name : str = ormar.String(max_length=100)
    type : str = ormar.String(max_length=100)
    value : str = ormar.String(max_length=100)


class Desk(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database, metadata=metadata
    )
    id : int = ormar.Integer(primary_key=True, autoincrement=True)
    name : str = ormar.String(max_length=100)
    description : str = ormar.Text()
    tasks : Optional[List[Task]] = ormar.ForeignKey(Task, related_name="tasks",  ondelete="CASCADE")
    additional_fields: Optional[List[TaskField]] = ormar.ForeignKey(TaskField, related_name="additional_field",  ondelete="CASCADE")





class User(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        metadata=metadata, database=database
    )

    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    firstName: str = ormar.String(max_length=100)
    lastName: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    password: SecretStr =  ormar.String(max_length=100)