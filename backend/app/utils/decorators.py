from functools import wraps
from flask import jsonify, session
from app.services.auth_service import get_current_user_id


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("Sessão atual:", session)
        print(get_current_user_id())
        if get_current_user_id() is None:
            print("entrei")
            return jsonify({"message": "Acesso não autorizado. Faça o login."}), 401
        return f(*args, **kwargs)

    return decorated_function
