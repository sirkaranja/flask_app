from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from models import Director, db

app= Flask(__name__)

#configuring sqlachemy in flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#for setting up migration in our db
migrate = Migrate(app, db)

#initialize our application for use within our databse configuration
db.init_app(app)


#view the deparments and directors
@app.route('/')
def index():
    response= make_response(
        '<h1>Hi welcome to KQ Company</h1>',
        200
    )
    return response

@app.route('/directors')
def all_directors():
    directors = Director.query.all()

    response_body = '<h1>Directors List</h1>'
    for director in directors:
        response_body += f'<h2>{director.name}</h2>'
    
    response = make_response(response_body, 200)
    return response
    
# @app.route('/')
# def index():
#     return '<h2 style="centre">Welcome to my first flask app</h2>'

# @app.route('/<string:username>')
# def user(username):
#     return f'<h3>Welcome user {username}</h3>'



if __name__ =='__main__':
    app.run(port=5506)