from random import choice as rc
from faker import Faker

from app import app
from models import db, Director, Department



fake= Faker()

with app.app_context():
    Director.query.delete()
    Department.query.delete()

    directors=[]
    for n in range(15):
        director= Director(name=fake.name())
        directors.append(director)

    db.session.add_all(directors)

    departments=[]
    depart_offices=['Accounting', 'Software Developer', 'Sports', 'Health','Finance','Human Resource']
    for n in range(30):
        depart= Department(name=fake.name(), specialization=rc(depart_offices))
        departments.append(depart)

    db.session.add_all(departments)
    db.session.commit()

    

