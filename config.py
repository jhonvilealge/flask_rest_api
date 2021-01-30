import os

# Absolute file path
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App
DEBUG = True
