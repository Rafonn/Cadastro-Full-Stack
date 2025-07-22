from flask import Blueprint, request, jsonify
from app.services import auth_service

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Usuário e senha são necessários"}), 400

    token = auth_service.attempt_login(data["username"], data["password"])

    if token:
        return jsonify({"token": token}), 200

    return jsonify({"message": "Credenciais inválidas"}), 401
