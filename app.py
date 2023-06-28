from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#in flask we import SQLALCHEMY class to contain all fileds as attributes such as Column, Integer
db = SQLAlchemy()

app= Flask(__name__)

#configuring sqlachemy in flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'


@app.route('/')
def index():
    return '<h2 style="centre">Welcome to my first flask app</h2>'

# @app.route('/<string:username>')
# def user(username):
#     return f'<h3>Welcome user {username}</h3>'



if __name__ =='__main__':
    app.run(port=5555)