from marshmallow import fields
from setup import db, ma 



class Location(db.Model):

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String,nullable=False)
    #latitude = db.Column(db.Float), nullable=False
    #longitude = db.Column(db.Float), nullable=False

    #assocations reciprocated
    #users = db.relationship('User', back_populates='locations')
    #libraries = db.relationship('Library', back_populates='locations')
#create marshamallow scheme to serialise table date into json format

class LocationSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name')
                  #calculating and printing distance - move to route)