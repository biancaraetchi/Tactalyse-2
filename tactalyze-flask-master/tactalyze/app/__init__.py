# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import matplotlib

import config

matplotlib.use('Agg')

# Define the WSGI application object
app = Flask(__name__)

from flask_simplelogin import SimpleLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'E*tY8N*3tV!EMr'
app.config['SIMPLELOGIN_USERNAME'] = 'loran@tactalyse'
app.config['SIMPLELOGIN_PASSWORD'] = 'randomCat@123'

with app.app_context():
    # Define the database object which is imported
    # by modules and controllers
    # Configurations
    app.config.from_object('config')
    db = SQLAlchemy(app)

    Session = db.session()


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.players.controllers import player_controller as player_mod


# Register blueprint(s)
app.register_blueprint(player_mod)

# app.register_blueprint(xyz_module)
# ..

SimpleLogin(app)
