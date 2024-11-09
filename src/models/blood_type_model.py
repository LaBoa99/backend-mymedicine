from peewee import IntegerField, CharField

from models.base_model import BaseModel

class BloodType(BaseModel):

    id = IntegerField(primary_key=True)
    blood_type = CharField(max_length=2, unique=True, null=False)

    