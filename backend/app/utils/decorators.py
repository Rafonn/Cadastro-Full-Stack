from functools import wraps
from flask import jsonify
from app.services.auth_service import get_current_user_id

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if get_current_user_id() is None:
            return jsonify({'message': 'Acesso não autorizado. Faça o login.'}), 401
        return f(*args, **kwargs)
    return decorated_function