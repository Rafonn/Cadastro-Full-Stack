from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from redis import Redis
import rq

from app.models.product import db
from app.controllers.auth_controller import auth_bp
from app.controllers.product_controller import product_bp


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "tech-solutio-secret-key-123"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:mpo69542507@localhost:5432/products"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["REDIS_URL"] = "redis://localhost:6379"

    db.init_app(app)
    Migrate(app, db)
    CORS(app, origins="http://localhost:4200", supports_credentials=True)

    # Configura a fila com Redis
    app.redis = Redis.from_url(app.config["REDIS_URL"])
    app.queue = rq.Queue("tech-solutio-tasks", connection=app.redis)

    # Registra os Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(product_bp, url_prefix="/api")

    return app
