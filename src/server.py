from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

from routes import simple_page  # Ensure `simple_page` is a Blueprint instance
from utils.utils import db

app = Flask(__name__)

# Configure the app
DATABASE:str = "roma"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:AXProduct2024@localhost:1401/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



##SQLAlchemy(app)
##db = SQLAlchemy(app, model_class=Base, disable_autonaming=True)
db.init_app(app)

with app.app_context():
    db.create_all()
app.register_blueprint(simple_page, url_prefix='/test')

if __name__ == "__main__":
    app.run(port=3000)
