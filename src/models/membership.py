
#Define model(table) for councils
class Council(db.Model):

    __tablename__ = "councils"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, varchar(50))

    location = db.Column(db.String)


#create marshamallow scheme to serialise table date into json format

class CouncilSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'location')