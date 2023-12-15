#Create Model for users
from marshmallow import fields

#Check imports

#Define model(table) for users
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, varchar(50))
    email = db.Column(db.String, varchar(50)), nullable=False
    location = db.Column(db.String)


#create marshamallow scheme to serialise table date into json format

class UserSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'email', 'location')
