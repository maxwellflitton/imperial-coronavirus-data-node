from flask import Blueprint

from src.models.user import User

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"


@user_views.route("/login", methods=['GET', 'POST'])
def login():
    return "login user view"


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
