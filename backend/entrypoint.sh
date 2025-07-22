#!/bin/sh

sleep 5

# Executa o comando para criar as tabelas no banco de dados.
echo "Criando as tabelas no banco de dados..."
python -c 'from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()'
echo "Tabelas criadas com sucesso."

exec gunicorn --bind 0.0.0.0:5000 run:app