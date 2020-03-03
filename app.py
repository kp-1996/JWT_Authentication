from flask import Flask
import logging.config
from db import db
from flask_restful import Api
from flask_jwt import JWT
from jwt_config.Jwt_config import authenticate, identity
from resources.user import User, Getusers
from resources.request_git import HTTPRequest

app = Flask('__name__')
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
log = logging.getLogger(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Prasad"
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/signup')
api.add_resource(Getusers, '/getusers')
api.add_resource(HTTPRequest, '/gitrequest')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    log.info("---Application started---")
    app.run(port=8080, debug = True)
