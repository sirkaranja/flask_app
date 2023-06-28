from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from models import db

app= Flask(__name__)

#configuring sqlachemy in flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#for setting up migration in our db
migrate = Migrate(app, db)

#initialize our application for use within our databse configuration
db.init_app(app)



@app.route('/')
def index():
    return '<h2 style="centre">Welcome to my first flask app</h2>'

# @app.route('/<string:username>')
# def user(username):
#     return f'<h3>Welcome user {username}</h3>'



if __name__ =='__main__':
    app.run(port=5504)