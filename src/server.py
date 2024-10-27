
from flask import Flask
from flask.blueprints import Blueprint
import routes
from models import db
from routes import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/test')
#db.init_app(server)
#db.app = server



if __name__ == "__main__":
    app.run(port=3000)
