#Create Model for users


#Check imports

#Define model(table) for users
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, varchar(50)
    email = db.Column(db.String), nullable=False
    location = db.Column(db.String)


#create marshamallow scheme to serialise table date into json format
