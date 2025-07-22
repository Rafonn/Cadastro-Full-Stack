import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get("REDIS_URL")

    # --- ADICIONE ESTAS LINHAS ABAIXO ---

    # Define explicitamente a política SameSite como 'Lax'.
    # 'Lax' permite que o cookie seja enviado em navegações de nível superior,
    # que é o que acontece quando seu Angular redireciona após o login.
    SESSION_COOKIE_SAMESITE = "Lax"

    # Garante que o cookie não exija uma conexão HTTPS,
    # já que estamos em ambiente de desenvolvimento (HTTP).
    SESSION_COOKIE_SECURE = False
