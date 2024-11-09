
from peewee import IntegerField, CharField, DateField, ForeignKeyField, SQL, CompositeKey

from models.base_model import BaseModel
from models.medical_record_model import MedicalRecord
from models.medicine_model import Medicine

class MedicalRecordToMedice(BaseModel):

    medical_record = ForeignKeyField(MedicalRecord, backref='medications', on_delete='CASCADE')
    medicine = ForeignKeyField(Medicine, backref='medical_records', on_delete='CASCADE')
    created_at = DateField(constraints=[SQL('DEFAULT CURRENT_DATE')])

    class Meta:
        primary_key = CompositeKey('medical_record', 'medicine')