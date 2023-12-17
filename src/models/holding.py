from marshmallow import fields
from setup import db, ma 

#Create holdings table

class Holding(db.Model):
    __tablename__ = 'holdings'

    ISBN = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

    #association library primary key
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'), nullable=False)
    library = db.relationship('Council', back_populates='holdings')

class HoldingSchema(ma.Schema):

    class Meta:
        fields = ('ISBN', 'title', 'author', 'availability')