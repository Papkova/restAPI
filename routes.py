from flask import jsonify, request
from . import app, db
from .models import User
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return jsonify({"message": "Hello, 7 group"})


class UserGet(Resource):
    def get(self):
        users = User.query.all()
        user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
        return jsonify(user_list)
