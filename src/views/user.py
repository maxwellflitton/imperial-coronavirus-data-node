from flask import Blueprint, render_template

user_views = Blueprint('user_views', __name__, template_folder='templates')


@user_views.route("/")
def user():
    return "basic user view"


@user_views.route("/login", methods=['GET', 'POST'])
def login():
    return ""

