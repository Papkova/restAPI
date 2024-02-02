import json
import os
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


load_dotenv()

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


api = Api(app)


from .models import User

from .routes import HelloWorld, UserGet


api.add_resource(HelloWorld, "/")
api.add_resource(UserGet, "/users")


SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:5000/swagger.json"
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "SAMPLE API"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

from . import routes