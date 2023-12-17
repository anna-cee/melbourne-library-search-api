
from marshmallow import fields
from setup import db, ma 

#Define model(table) for librarys
class Library(db.Model):

    __tablename__ = "libraries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

    #Association with council_id
    council_id = db.Column(db.Integer, db.ForeignKey('councils.id'), nullable=False)
    user = db.relationship('Council', back_populates='libraries')
    #Association with location
    location_id = db.Column(db.String, db.ForeignKey('locations.id_seq'), nullable=False)
    location = db.relationship('Location', back_populates='libraries')
    holdings = db.relationship('Holdings', back_populates='libraries')




#create marshamallow scheme to serialise table date into json format

class LibrarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location')