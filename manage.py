# application entry point

import os

from flask_script import Manager

from app import create_app

app = create_app(os.getenv('APP_SETTING') or 'production')

# Instantiate manager with flask instance
manager = Manager(app)
