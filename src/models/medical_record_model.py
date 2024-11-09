from peewee import IntegerField, CharField, DateField, ForeignKeyField

from models.base_model import BaseModel
from models.user_model import User
from models.blood_type_model import BloodType

class MedicalRecord(BaseModel):

    id = IntegerField(primary_key=True)
    name = CharField(max_length=255, null=False)
    paternal_surname = CharField(max_length=255, null=False)
    mother_surname = CharField(max_length=255, null=False)
    sex_assigned = CharField(max_length=1, null=False)
    birth_date = DateField(null=False)

    user = ForeignKeyField(User, backref='medicalRecords', null=False, on_delete='CASCADE')
    blood_type = ForeignKeyField(BloodType, backref='medicalRecords', null=True, on_delete='SET NULL')
