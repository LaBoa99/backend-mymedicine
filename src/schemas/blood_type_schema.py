
from marshmallow_peewee import ModelSchema

from models.blood_type_model import BloodType

class BloodTypeSchema(ModelSchema):
    
    class Meta:
        model = BloodType