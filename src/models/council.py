from setup import db, ma 
from marshmallow import fields

#Define model(table) for councils
class Council(db.Model):

    __tablename__ = "councils"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, default='12345678')
    is_admin = db.Column(db.Boolean, default=False)
    


#create marshamallow scheme to serialise table date into json format

class CouncilSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'email', 'is_admin','location')