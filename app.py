from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return '<h2 style="centre">Welcome to my first flask app</h2>'

@app.route('/<string:username>')
def user(username):
    return f'<h3>Welcome user {username}</h3>'



if __name__ =='__main__':
    app.run(port=5555)