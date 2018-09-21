# from flask_api import FlaskAPI

from instance.config import app_config
from app.api import app

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')
    app.secret_key = '5c750c0e72ce5394dfe7720fa26d0327d616ff9ff869be19'
    app.config['SESSION_TYPE'] = 'filesystem'
    return app