from flask import flask
from flask_bootstrap import Bootstrap


bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__)

    #initializing extensions
    bootstrap.init_app(app)
