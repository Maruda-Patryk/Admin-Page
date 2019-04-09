
import os

class Config(object):
    RECAPTCHA_PUBLIC_KEY = ""
    RECAPTCHA_PRIVATE_KEY = ""

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'asdasfhsgdajsgfygasda'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost:3306/admin_page'
    PORT = 8080

class ProdConfig(Config):
    pass