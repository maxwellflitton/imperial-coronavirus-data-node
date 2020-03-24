from flask import Flask, render_template, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user, logout_user

from src.views.user import user_views
from src.models.trust import Trust
from src.models.user import User
from src.database import DbEngine
from src.forms import LoginForm


app = Flask(__name__, template_folder='./src/templates', static_folder="./src/static")
db = DbEngine()

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
login = LoginManager(app)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", title="Log-In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

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
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Trust, db.session))


if __name__ == "__main__":
    app.run()
