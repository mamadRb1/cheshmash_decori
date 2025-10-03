import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key_here')
SQLALCHEMY_DATABASE_URI = 'postgresql://cheshmash_produciton_url_here'
SQLALCHEMY_TRACK_MODIFICATIONS = False
