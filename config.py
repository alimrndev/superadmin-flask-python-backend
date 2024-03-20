import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))

    BASE_URL = str(os.environ.get("BASE_URL"))
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    JWT_BLACKLIST_ENABLED = True

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}" 
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS",
        True if os.environ.get("FLASK_ENV") in ("prod", "production") else False,
    )

    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 #Max Size = 10 MB
    