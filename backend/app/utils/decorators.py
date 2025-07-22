from functools import wraps
from flask import request, jsonify, g
from app.services.auth_service import verify_token


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token não encontrado!"}), 401

        user_id = verify_token(token)

        try:
            user_id_int = int(user_id)
        except (ValueError, TypeError):
            return jsonify({"message": "ID de usuário inválido"}), 401

        g.user_id = user_id_int

        return f(*args, **kwargs)

    return decorated_function
