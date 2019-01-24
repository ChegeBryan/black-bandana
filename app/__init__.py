"""
app/__init__.py
creation of application factory
"""

from flask import Flask
from flask import Blueprint
from flask_restplus import Api


from instance.config import config_environment
from api.controller.user_controller import api as user_ns

def create_app(config_name):
    """
    App creation function
    :param: environment name
    :return: flask object
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_environment[config_name])
    
    blueprint = Blueprint('api', __name__)

    api = Api(blueprint, 
        title="Black Bandana Authorization RESTful API with JWT",
        version="1.0",
        description="A RESTful API built with Flask"
    ) 

    # add user namespace to the namespaces and define the prefix url
    api.add_namespace(user_ns, path='api/v1')

    return app

