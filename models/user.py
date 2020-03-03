from db import db
import sqlite3
import logging

log = logging.getLogger(__name__)

class Usermodel(db.Model):
    log.info("---User Module started---")
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {"ID":self.id, "Username":self.username, "password":self.password}

    def save(self):
        db.session.add(self)
        db.session.commit()
        log.info("Data saved {}".format(self))

    @classmethod
    def find_by_name(cls, name):
        log.info("---User Module find_by_name method started---")
        return cls.query.filter_by(username=name).first()

    @classmethod
    def find_by_id(cls, _id):
        log.info("---User Module find_by_id method started---")
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find(cls):
        log.info("---User Module find method started---")
        return  {"users":list(map(lambda x: x.json(), cls.query.all()))}
