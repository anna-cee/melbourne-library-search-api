from marshmallow import fields
from setup import db, ma 
#Define model(table) for memberships
class Membership(db.Model):

    __tablename__ = "memberships"

    membership_number = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date)
   

    #Association with user_id
    #Association with council_id


#create marshamallow scheme to serialise table date into json format

class MembershipSchema(ma.Schema):

    class Meta:
        fields = ('membership_number', 'date_created')