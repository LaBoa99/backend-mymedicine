from peewee import IntegerField, CharField

from models.base_model import BaseModel


class Medicine(BaseModel):

    id = IntegerField(primary_key=True)
    
    name = CharField(max_length=255, null=False)
    formule = CharField(max_length=255, unique=True, null=True)
    laboratory = CharField(max_length=255, null=True)
    alternative = CharField(max_length=255, null=True)
    dose_interval = CharField(max_length=16, null=False)
    
    total_doses = IntegerField(null=False)
    current_doses = IntegerField(null=False, default=0)

