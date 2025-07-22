from app import create_app
from app.models.product import db
from dotenv import load_dotenv

load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()
app.run(debug=True)