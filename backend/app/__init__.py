from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from redis import Redis
import rq

from app.config import Config
from app.models.product import db
from app.controllers.auth_controller import auth_bp
from app.controllers.product_controller import product_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa extensões
    db.init_app(app)
    Migrate(app, db)
    CORS(app, supports_credentials=True) # Habilita CORS para o frontend

    # Configura a fila com Redis [cite: 5]
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.queue = rq.Queue('tech-solutio-tasks', connection=app.redis)

    # Registra os Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(product_bp, url_prefix='/api')
    
    return app