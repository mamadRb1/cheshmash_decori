import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
from models import Product, db

product_bp = Blueprint('products', __name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@product_bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'price': p.price,
        'image': p.image
    } for p in products])

@product_bp.route('/', methods=['POST'])
@jwt_required()
def add_product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    image = request.files.get('image')

    filename = None
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))

    new_product = Product(name=name, description=description, price=float(price), image=filename)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'msg': 'Product added successfully'}), 201

@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    image = request.files.get('image')

    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = float(price)
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, filename))
        product.image = filename

    db.session.commit()
    return jsonify({'msg': 'Product updated successfully'})

@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'msg': 'Product deleted successfully'})
