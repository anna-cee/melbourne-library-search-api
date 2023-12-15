from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


app = Flask(__name__)


#add db key

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://lib_search_dev:GorillaLibrarianFibbs789@127.0.0.1:5432/melb_lib_search_api"


db = SQLAlchemy(app)
ma = Marshmallow(app)

message = 'Hello, world!'

@app.route('/')
def index():
    return ('test is okay, 201')

if __name__ == '__main__':
   app.run(debug=True, port=5000)