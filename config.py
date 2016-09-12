import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://test_user:re@localhost/test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False