""" The config module has all api configurations """
import os
from typing import Dict

from flask import Flask


class Config:
    """ Contains configurations common to all environments """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    SALT = os.environ.get("APP_SALT")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_EXPIRY = 15552000
    ENV = os.environ.get("ENVIRONMENT")
    SQLALCHEMY_ECHO = False
    SHOW_GRAPHIQL = True

    @classmethod
    def init_app(self, app: Flask):
        app.config.from_object(self)


class DevelopmentConfig(Config):
    """Has configurations used during development"""

    DEBUG = True
    PORT = os.environ.get("PORT")
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """ Has configurations used during testing """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("APP_TEST_DATABASE_URI")
    TOKEN_EXPIRY = 0.5


class ProductConfig(Config):
    """ Has configuration for use during Production """

    SHOW_GRAPHIQL = False


CONFIGS: Dict[str, Config] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductConfig,
    "default": DevelopmentConfig,
}