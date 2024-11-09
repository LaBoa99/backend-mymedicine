import os

from flask import Flask
from db import Database
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager


# Routes
from routes.user_routes import user_bp

app = Flask(__name__)

endpoints = [
    user_bp
]

for endpoint in endpoints:
    app.register_blueprint(endpoint, url_prefix='/api')

# Config
load_dotenv()  # Cargar las variables desde .env
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_TOKEN_LOCATION'] = [ os.getenv('JWT_TOKEN_LOCATION') ]
jwt = JWTManager(app)

if __name__ == '__main__':
    Database.init_db()
    app.run(debug=True)



