from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ


app = Flask(__name__)

#JWT Key
app.config['JWT_KEY'] = environ.get('JWT_KEY')


#add db key
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

message = 'Hello, world!'

@app.route('/')
def index():
    return ('test is okay, 201')

if __name__ == '__main__':
   app.run(debug=True, port=5000)