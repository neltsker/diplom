import ormar
from typing import Optional, List
import config
from auth.models import User
import sqlalchemy
import databases
from typing import ForwardRef

database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()

TaskRef = ForwardRef("Task")

class Task(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database, metadata=metadata, tablename="tasks"
    )

    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    author: User = ormar.ForeignKey(User, related_name="author")
    name : str = ormar.String(max_length=100)
    description : str = ormar.Text()
    executor : User = ormar.ForeignKey(User, related_name="executor")
    viewers : Optional[List[User]] = ormar.ManyToMany(User, related_name="viewers")
    #another : str = ormar.String(max_length=100)
    type: str = ormar.String(max_length=100)
    related_tasks : TaskRef = ormar.ForeignKey(TaskRef, related_name="related_tasks")

Task.update_forward_refs()