import os
from app import create_app
from app.models.product import db

# --- DEFINIÇÃO MANUAL DAS VARIÁVEIS DE AMBIENTE ---
# Substitua os valores abaixo pelos seus dados reais.
# Esta abordagem garante que as variáveis existam antes da criação do app.

os.environ["SECRET_KEY"] = "tech-solutio-secret-key-123"

os.environ["DATABASE_URL"] = "postgresql://postgres:mpo69542507@localhost:5432/products"

os.environ["REDIS_URL"] = "redis://localhost:6379"
# ----------------------------------------------------


# Agora, criamos a aplicação. Ela lerá as variáveis que acabamos de definir.
app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # Cria as tabelas se não existirem
        db.create_all()
    app.run(debug=True)
