from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Director(db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    department = db.relationship('Department', backref='directors')

    def __repr__(self):
        return f'<Department Director {self.name}>'

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    specialization = db.Column(db.String)

    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))

    def __repr__(self):
        return f'<Department {self.name}, {self.specialization}>'
