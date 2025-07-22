import jwt
import datetime

# !! APENAS PARA DEPURAÇÃO !!
# Usando a chave diretamente no código para eliminar o Flask config como variável.
HARDCODED_SECRET = "tech-solutio-secret-key-123"

# Usuário e senha fictícios
HARDCODED_USER = {"username": "admin", "password": "password123", "id": 1}


def generate_token(user_id):
    """Gera o Token de Autenticação usando a chave hardcoded."""
    print(f"[GENERATE] Usando chave hardcoded: '{HARDCODED_SECRET}'")
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, HARDCODED_SECRET, algorithm="HS256")
    except Exception as e:
        return e


def verify_token(token):
    """Verifica o token usando a chave hardcoded."""
    print(f"[VERIFY] Usando chave hardcoded: '{HARDCODED_SECRET}'")
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
