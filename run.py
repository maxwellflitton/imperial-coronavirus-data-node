from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.views.user import user_views
from src.config import GlobalParams


params = GlobalParams()
app = Flask(__name__, template_folder='src/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = params.get("DB_URL")
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)


def import_models(database) -> None:
    """
    Imports the models to create the tables in the database

    :return: None
    """
    from models.user import User
    database.create_all()


@app.route("/")
def home():
    return "this is a data processing node"


app.register_blueprint(user_views, url_prefix="/users")


if __name__ == "__main__":
    import_models(database=db)
    # app_instance.import_models()
    app.run()
