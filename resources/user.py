from flask_restful import Resource, reqparse
from models.user import Usermodel
from flask_jwt import jwt_required
import json
import logging

log = logging.getLogger(__name__)

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str, help='This field can not be Empty')
    parser.add_argument('password', required=True, type=str, help='This field can not be Empty')

    def post(self):
        data = User.parser.parse_args()
        log.info("{}".format(data))
        if Usermodel.find_by_name(data['username']):
            log.warning("User with name {} is already exists".format(data['username']))
            return {"message":"User with name {} is already exists".format(data['username'])}
        user = Usermodel(**data)
        user.save()
        return user.json()

class Getusers(Resource):
    def get(self):
        data = Usermodel.find()
        log.info("{} ".format(json.dumps(data)))
        return data
