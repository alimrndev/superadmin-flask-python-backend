from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Initialize Config
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize DB Migrate
migrate = Migrate(app, db)

# Initialize JWTManager
jwt = JWTManager(app)

from app.model import user, dosen, mahasiswa, image
from app import routes