# -*- coding: utf-8 -*-
import os
import sys
# -----------------------------
#  COMMON CONFIG
# -----------------------------

basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


# ENVIRONMENT (development, production)
ENVIRONMENT = 'development'

# DEFAULT URL
DEFAULT_URL = 'http://0.0.0.0:3000'

# LOGGER FORMATTING
LOGGER_FORMAT = '[%(levelname)s][%(filename)s:%(lineno)s] %(message)s'


# -----------------------------
#  APP CONFIG
# -----------------------------

# APP DEFAULT PORT (default : 5000)
APP_DEFAULT_PORT = 3000

# APP SECRET KEY
# APP_SECRET_KEY = 'APP_SECRET_KEY'
if os.environ.get('APP_SECRET_KEY'):
	APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY')
else:
	APP_SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
	print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

# TOKEN
TOKEN_SCHEME = "bearer"
TOKEN_EXPIRE_TIME = 60 * 60 * 24 * 30 * 6


# -----------------------------
#  API CONFIG
# -----------------------------

# API VERSION
API_VERSION = 1

# API ACCEPT HEADER
API_ACCEPT_HEADER = 'application/json'


# -----------------------------
#  MOBILE APPLICATION CONFIG
# -----------------------------

# APPLICATION VERSION
APP_VERSION = '1.0.0'


# -----------------------------
#  DATABASE CONFIG
# -----------------------------



# DATABASE URL & SETTING
DATABASE = {
    'engine': os.getenv('DB_ENGINE') or 'postgres',
    'host': os.getenv('DB_HOST') or 'localhost',
    'port': os.getenv('DB_PORT') or '5432',
    'user': os.getenv('DB_USER') or '',
    'password': os.getenv('DB_PASSWORD') or '',
    'database': os.getenv('DB_DATABASE') or ''
}
"""
DATABASE = {
    'engine': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'user': '',
    'password': '',
    'database': ''
}
"""
DATABASE_URI = '%(engine)s://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s' % DATABASE