from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from  models.user_model import User

def jwt_auth(fn):

    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()

        # Verificar si el usuario existe en la base de datos
        user_exists = User.select().where(User.id == user_id).exists()

        if not user_exists:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        return fn(*args, **kwargs)
    
    return wrapper