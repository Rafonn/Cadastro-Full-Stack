from flask import Blueprint, request, jsonify
from app.services import product_service
from app.utils.decorators import login_required

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
@login_required
def create_product():
    data = request.get_json()
    product, message = product_service.create_product(data)
    if not product:
        return jsonify({'message': message}), 400
    return jsonify(product.to_dict()), 201

@product_bp.route('/products', methods=['GET'])
@login_required
def get_products():
    products = product_service.get_all_products()
    return jsonify([p.to_dict() for p in products]), 200

@product_bp.route('/products/<int:id>', methods=['PUT'])
@login_required
def update_product(id):
    product = product_service.get_product_by_id(id)
    if not product:
        return jsonify({'message': 'Produto não encontrado'}), 404
    
    data = request.get_json()
    updated_product = product_service.update_product(product, data)
    return jsonify(updated_product.to_dict()), 200

@product_bp.route('/products/<int:id>', methods=['DELETE'])
@login_required
def delete_product(id):
    product = product_service.get_product_by_id(id)
    if not product:
        return jsonify({'message': 'Produto não encontrado'}), 404
    
    product_service.delete_product(product)
    return jsonify({'message': 'Produto excluído com sucesso'}), 200