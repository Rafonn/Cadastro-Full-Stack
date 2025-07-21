from flask import session

# Usuário e senha fictícios, como permitido no requisito.
HARDCODED_USER = {
    'username': 'admin',
    'password': 'password123'
}

def login_user(username, password):
    """Verifica as credenciais e inicia a sessão."""
    if username == HARDCODED_USER['username'] and password == HARDCODED_USER['password']:
        session.clear()
        session['user_id'] = 1
        return True
    return False

def logout_user():
    """Limpa a sessão do usuário."""
    session.clear()

def get_current_user_id():
    """Retorna o ID do usuário logado."""
    return session.get('user_id')