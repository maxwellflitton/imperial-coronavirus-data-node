from flask import Blueprint
from flask import request, jsonify, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user

from src.models.user import User
from src.database import DbEngine

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"


@user_views.route("/login", methods=['POST'])
def login():
    body = request.get_json()
    db = DbEngine()
    user_check = db.session.query(User).filter(User.username == body.get("username", "")).one_or_none()
    if user_check is None or user_check.check_password(password=body.get("password", "")) is False:
        return jsonify({"success": False})

    login_user(user_check)
    return jsonify({"success": True})


@user_views.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@user_views.route("/dashboard", methods=['GET'])
def dashboard():
    if current_user.is_authenticated:
        return render_template("dashboard.html", user=current_user)
    return redirect(url_for('home'))


@user_views.route("/create/<username>/<email>/<password>", methods=['GET', 'POST'])
def create_user(username, email, password):
    """
    Basic view that creates a user, to be refactored to just POST with body.

    :param username: (str) the username of the user model instance to be created
    :param email: (str) the email of the user model instance to be created
    :param password: (str)
    :return:
    """
    user_instance = User(username=username, email=email, password=password)
    user_instance.save_instance()
    return {"username": user_instance.username, "email": user_instance.email}
