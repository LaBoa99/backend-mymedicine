from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from middlewares.auth import jwt_auth
from models.user_model import User
from schemas.user_schema import UserSchema

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import bcrypt


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def register():
    json_data = request.get_json()
    schema = UserSchema()
    try:
        data: UserSchema = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    email_in_use = User.select().where(User.email == data.email).exists()
    if email_in_use:
        return jsonify({"error": "El correo ya está en uso."}), 400

    hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())

    try:
        user = User.create(email=data.email, password=hashed_password.decode('utf-8'))
    except Exception:
        return jsonify({"error": "Error al crear el usuario."}), 500
    
    return jsonify(schema.dump(user)), 201

@user_bp.route('/users/login', methods=['POST'])
def login():
    json_data = request.get_json()
    schema = UserSchema()
    try:
        data: UserSchema = schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    user = User.select().where(User.email == data.email).first()
    if user and bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({"error": "Error al autenticar."}), 401

@user_bp.route('/users-2', methods=['GET'])
@jwt_auth
def get_all_auth():
    user_id = get_jwt_identity()
    user = User.select().where(User.id == user_id).exists()
    if user:
        users = User.select()
        schema = UserSchema(exclude=('password',))
        return jsonify(schema.dump(users, many=True)), 200
    return {}, 200

@user_bp.route('/users', methods=['GET'])
def get_all():
    users = User.select()
    schema = UserSchema(exclude=('password',))
    return jsonify(schema.dump(users, many=True)), 200