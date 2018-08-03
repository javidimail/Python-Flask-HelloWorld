from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
 return 'Hey its Python Flask application! I am in python2!!'

if __name__ == '__main__':
 app.run()
