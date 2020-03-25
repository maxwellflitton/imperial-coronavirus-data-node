from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

from src.views.user import user_views
from src.views.admin import TrustView, UserView
from src.models.trust import Trust
from src.models.user import User
from src.database import DbEngine


app = Flask(__name__, template_folder='./src/templates', static_folder="./src/static")
db = DbEngine()

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
login = LoginManager(app)


@login.user_loader
def load_user(id):
    user = db.session.query(User).filter(User.id == id).one_or_none()
    return user


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/createdb")
def create():
    """
    Fire to create the database table.
    :return: View str
    """
    db.create_tables()
    return "db created"


app.register_blueprint(user_views, url_prefix="/users")
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(UserView(User, db.session))
admin.add_view(TrustView(Trust, db.session))


if __name__ == "__main__":
    app.run()
