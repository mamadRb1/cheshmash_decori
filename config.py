import os

SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_here')
SQLALCHEMY_DATABASE_URI = 'postgresql://cheshmash_products_db_user:vJggUZnjphGCrDUilf13cYAu0Ox2uSmz@dpg-d3ffaj2dbo4c73a7n2lg-a:5432/cheshmash_products_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
