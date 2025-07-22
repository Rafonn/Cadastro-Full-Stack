import jwt
import datetime
import os

from dotenv import load_dotenv

load_dotenv()

HARDCODED_SECRET = os.getenv("SECRET_KEY")
HARDCODED_USER = {"username": "admin", "password": "password123", "id": 1}


def generate_token(user_id):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": str(user_id),
        }
        return jwt.encode(payload, HARDCODED_SECRET, algorithm="HS256")
    except Exception as e:
        return e


def verify_token(token):
    try:
        payload = jwt.decode(token, HARDCODED_SECRET, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return "Token expirado. Por favor, faça login novamente."
    except jwt.InvalidTokenError:
        return "Token inválido. Por favor, faça login novamente."


def attempt_login(username, password):
    """Verifica as credenciais e retorna um token se forem válidas."""
    if (
        username == HARDCODED_USER["username"]
        and password == HARDCODED_USER["password"]
    ):
        return generate_token(HARDCODED_USER["id"])
    return None
