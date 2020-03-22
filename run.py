from flask import Flask, render_template
from flask_login import LoginManager

from src.views.user import user_views
from src.config import GlobalParams


app = Flask(__name__, template_folder='src/templates')
app.config['SECRET_KEY'] = 'mysecretkey'
# login = LoginManager(app)


@app.route("/")
def home():
    return "this is a data processing node"


@app.route("/createdb")
def create():
    """
    Fire to create the database table.
    :return: View str
    """
    from src.database import DbEngine
    db = DbEngine()
    db.create_tables()
    return "db created"


app.register_blueprint(user_views, url_prefix="/users")


if __name__ == "__main__":
    app.run()
