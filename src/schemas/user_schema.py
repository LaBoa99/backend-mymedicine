from marshmallow_peewee import ModelSchema
from marshmallow import fields, validates, ValidationError
from marshmallow.validate import Email
from models.user_model import User

class UserSchema(ModelSchema):
    
    class Meta:
        model = User

    # Solo lectura
    id = fields.Int(dump_only=True)
    # Solo escritura
    password = fields.Str(required=True, load_only=True)
    email = fields.Str(required=True, validate=Email(error="Dbee ser un correo electronico valido"))

    @validates('password')
    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres")
            