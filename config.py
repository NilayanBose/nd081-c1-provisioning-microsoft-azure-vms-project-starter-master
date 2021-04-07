import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorageacc'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Uvl2FPxemV5NIl9evvjz2o3VYyYjxPCKLW6dRjMQWQuaB42Djql8JFwo2jkyHa1RW+tBY3AHjY+WcvSUjjGsww=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'testcmsserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'usr'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'welcome@1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = os.getenv("CLIENT_SECRET") or 'P4D__vT_62wh0f~.f72G9LwqQFf.Qd~obb'
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/9ab75c1d-a904-4862-af8a-d1c7903df9f8"

    CLIENT_ID = os.getenv("CLIENT_ID") or 'a4aaa8d6-74f9-424f-8759-9ecc30388610'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session