from flask import Blueprint, request, jsonify
from app.services import auth_service

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Usuário e senha são necessários'}), 400

    if auth_service.login_user(data['username'], data['password']):
        return jsonify({'message': 'Login bem-sucedido'}), 200
    
    return jsonify({'message': 'Credenciais inválidas'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    auth_service.logout_user()
    return jsonify({'message': 'Logout bem-sucedido'}), 200