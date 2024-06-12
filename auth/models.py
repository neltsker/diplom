from typing import Optional
import ormar
import sqlalchemy
import databases
import config
from pydantic import SecretStr
#from database.db import metadata#, database

database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()




class User(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        metadata=metadata, database=database
    )

    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    firstName: str = ormar.String(max_length=100)
    lastName: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    password: SecretStr =  ormar.String(max_length=100)
