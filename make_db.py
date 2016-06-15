#!flask/bin/python
from app import db, models
from config import SQLALCHEMY_DATABASE_URI

db.create_all()

