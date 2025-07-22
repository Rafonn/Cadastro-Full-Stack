from functools import wraps
from flask import request, jsonify, current_app  # Importe current_app
from app.services.auth_service import verify_token


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization")

        # --- ADICIONE OS PRINTS DE DEPURAÇÃO AQUI ---
        print("--- Depurando @login_required ---")
        print(f"Cabeçalho Authorization recebido: {auth_header}")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        print(f"Token extraído: {token}")
        print(
            f"SECRET_KEY que será usada para verificar: {current_app.config.get('SECRET_KEY')}"
        )
        print("---------------------------------")
        # --- FIM DOS PRINTS ---

        if not token:
            return jsonify({"message": "Token não encontrado!"}), 401

        user_id = verify_token(token)
        if not isinstance(user_id, int):
            return jsonify({"message": user_id}), 401

        return f(*args, **kwargs)

    return decorated_function
