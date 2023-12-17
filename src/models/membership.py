from marshmallow import fields
from setup import db, ma 
#Define model(table) for memberships
class Membership(db.Model):

    __tablename__ = "memberships"

    number = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.String)
   

    #Association with user_id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='memberships')
    #Association with council_id
    council_id = db.Column(db.Integer, db.ForeignKey('councils.id'), nullable=False)
    council = db.relationship('Council', back_populates='memberships')


#create marshamallow scheme to serialise table date into json format

class MembershipSchema(ma.Schema):

    class Meta:
        fields = ('membership_number', 'date_created')