from peewee import IntegerField, CharField

from models.base_model import BaseModel


class User(BaseModel):
    id = IntegerField(primary_key=True)
    password = CharField(max_length=255, null=False)
    email = CharField(max_length=255, unique=True, null=False)

