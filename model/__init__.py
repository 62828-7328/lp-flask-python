from app import app, db
from model.user import *
from model.client import *
from model.os import *


with app.app_context():
    db.create_all()