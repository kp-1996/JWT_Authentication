from flask_restful import Resource
from flask_jwt import jwt_required
import requests

class HTTPRequest(Resource):
    @jwt_required()
    def get(self):
        url = 'https://api.github.com'
        response = requests.get(url)
        return response.json()
