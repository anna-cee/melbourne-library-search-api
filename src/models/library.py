
#Define model(table) for librarys
class Library(db.Model):

    __tablename__ = "libraries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, varchar(50))
    location = db.Column(db.String)

    #association with council


#create marshamallow scheme to serialise table date into json format

class LibrarySchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'location')