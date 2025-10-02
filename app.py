from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

# Load config
app.config.from_object('config')

# Init extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Create uploads folder
os.makedirs('static/uploads', exist_ok=True)

# Import blueprints
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
