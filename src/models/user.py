#Create Model for users
from marshmallow import fields
from setup import db, ma 


#Define model(table) for users with User class
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String, nullable=False, default='None')
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    location = db.Column(db.String, nullable=True)

    #assocations with locations table
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    location = db.relationship('Location', back_populates='users')
    #membership = db.relationship('Membership', back_populates='users')
    



#create marshamallow scheme to serialise table date into json format

class UserSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'location')
