from peewee import SqliteDatabase\

from common.blood_types import BLOOD_TYPES
from models.medical_record_model import User, MedicalRecord, BloodType
from models.medical_record_medicine_model import MedicalRecordToMedice, Medicine

db = SqliteDatabase('database.db')

class Database:

    @staticmethod
    def init_db():
        db.connect()
        db.create_tables([
            User,
            Medicine,
            MedicalRecord,
            BloodType,
            MedicalRecordToMedice
        ], safe=True)

        # Insert enum of blood types
        bloods_in_db = [ blood['blood_type'] for blood in BloodType.select().dicts() ]
        for blood in BLOOD_TYPES:
            if not blood in bloods_in_db:
                BloodType.insert({'blood_type': blood}).execute()

        db.close()