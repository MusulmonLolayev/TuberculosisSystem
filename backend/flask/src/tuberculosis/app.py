from flask import Flask
from .settings import DEBUG, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from flask_migrate import Migrate

# app object
app = Flask(__name__)
app.config.from_object('tuberculosis.settings')

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Admin panel', template_mode='bootstrap3')

# Data base object
db = SQLAlchemy(app)

# Initialize Marshmallow for API
ma = Marshmallow(app)

# default-index url
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# register apps
from patient import patient
from auth import auth
app.register_blueprint(patient) 
app.register_blueprint(auth) 


# set optional bootswatch theme for admin panel
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

migrate = Migrate(app, db)

def create_app():
    db.create_all()
    return app