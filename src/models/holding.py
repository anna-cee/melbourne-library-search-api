#Check imports

#Create holdings table

class Holding(db.Model):
    __tablename__ = 'holdings'

    ISBN = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)

    #association library primary key

class HoldingSchema(ma.SchemataSchema):

    class Meta:
        fields = ('ISBN', 'title', 'author', 'availability')