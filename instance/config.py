# app environment variables settings
import os


class Config:
    """
    Global configurations environment variables
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET', 'my_precious_gollum')


class DevelopmentConfig(Config):
    """ Modify Environment variables for development """
    DEBUG = True


class ProductionConfig(Config):
    """ Modify environment variable for production """
    DEBUG = False
    TESTING = False

