from tuberculosis.app import db
from flask_login import UserMixin
from common.models import Base
from flask_admin.contrib.sqla import ModelView

# Define User data-model
class User(UserMixin, Base):
    __tablename__ = 'users'

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # Relationships
    roles = db.relationship('Role', secondary='user_roles')

    def __init__(self):
        super.name = self.last_name + " " + first_name + " " + self.middle_name
        
    def __str__(self):
        return self.last_name + " " + first_name + " " + self.middle_name

# Define the Role data-model
class Role(Base):
    __tablename__ = 'roles'

# Define the UserRoles association table
UserRoles = db.Table(
    'user_roles',
    db.Column('id', db.Integer(), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
)