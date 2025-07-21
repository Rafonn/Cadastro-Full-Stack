from app.models.product import db, Product
from flask import current_app

def log_task(message):
    """Função simples que será executada pela fila do Redis."""

    print(message)

def get_all_products():
    """Retorna todos os produtos do banco de dados."""

    return Product.query.all()

def get_product_by_id(product_id):
    """Busca um produto pelo seu ID."""

    return Product.query.get(product_id)

def create_product(data):
    """Cria um novo produto e o salva no banco."""

    if not all(k in data for k in ['name', 'brand', 'value']):
        return None, "Campos 'name', 'brand', e 'value' são obrigatórios."
    if not isinstance(data['value'], (int, float)) or data['value'] <= 0:
        return None, "O valor do produto deve ser um número positivo."

    new_product = Product(
        name=data['name'],
        brand=data['brand'],
        value=data['value']
    )
    db.session.add(new_product)
    db.session.commit()
    
    current_app.queue.enqueue(log_task, f"Produto criado: {new_product.name}")
    
    return new_product, "Produto criado com sucesso."

def update_product(product, data):
    """Atualiza os dados de um produto existente."""

    product.name = data.get('name', product.name)
    product.brand = data.get('brand', product.brand)
    product.value = data.get('value', product.value)
    db.session.commit()
    return product

def delete_product(product):
    """Remove um produto do banco de dados."""
    
    db.session.delete(product)
    db.session.commit()