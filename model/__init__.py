from app import app, db
from model.user import *
from model.client import *
from model.os import *
from model.service import *


with app.app_context():
    db.create_all()