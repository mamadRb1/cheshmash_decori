from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

# Load config
app.config.from_object('config')

# Init extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Cheshmash Decori API 💜✨",
        "status": "ok"
    })

# Create uploads folder
os.makedirs('static/uploads', exist_ok=True)

# Blueprints
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/product')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # فقط برای اولین بار ساخت جداول
    app.run(host='0.0.0.0', port=5000)
