
import os

class Config(object):
    pass

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'asdasfhsgdajsgfygasda'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    PORT = 8080

class ProdConfig(Config):
    pass