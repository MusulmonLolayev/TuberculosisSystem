from flask import Blueprint
auth = Blueprint('auth', __name__)
from .models import User, Role, UserRoles
from tuberculosis.app import admin, db
from flask_admin.contrib.sqla import ModelView
admin.add_views(ModelView(User, db.session))
admin.add_views(ModelView(Role, db.session))
from . import models