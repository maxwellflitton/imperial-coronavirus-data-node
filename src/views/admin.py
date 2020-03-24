from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash

from src.models.user import User
from src.database import DbEngine


class UserView(ModelView):

    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    create_modal = True
    edit_modal = True
    form_excluded_columns = ['unique_id', 'credit_amount']
    column_exclude_list = ['unique_id', 'credit_amount', 'password']

    def create_model(self, form) -> User:
        """
        Fires just before the model is created.

        :param form: (flask.Form) data being passed from the admin front-end
        :return: (User) model with attributes to be saved
        """
        new_user = User(username=form.data["username"], email=form.data["email"], password=form.data["password"],
                        admin=form.data["admin"], trust_id=form.data["trust"].id)
        new_user.save_instance()
        return new_user

    def update_model(self, form, model) -> bool:
        """
        Fires just before the model is edited.

        :param form: (flask.Form) data being passed from the admin front-end
        :param model: (User) model to be updated
        :return: (bool) True is successful
        """
        db = DbEngine()
        user_from_db = db.session.query(User).filter(User.id == model.id).one_or_none()

        model.username = form.data["username"]
        model.email = form.data["email"]
        model.admin = form.data["admin"]
        model.trust_id = form.data["trust"].id

        if form.data["password"] != user_from_db.password:
            model.password = generate_password_hash(password=form.data["password"])
        return True


class TrustView(ModelView):

    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    create_modal = True
    edit_modal = True
