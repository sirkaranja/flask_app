from random import choice as rc
from faker import Faker

from app import app
from models import db, Director, Department

db.init_app(app)

fake= Faker()

with app.app_context():
    Director.query.delete()
    Department.query.delete()

    

