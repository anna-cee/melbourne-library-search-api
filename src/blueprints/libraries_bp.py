

#create blueprint

librarys_bp = Blueprint('librarys', __name__)


#get list of libraries
@librarys_bp.route('/')
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all()
    return LibraryScheme(many=True).dump(libraries)


#get libraries close to user locaiton - libraries/near_me
@librarys_bp.route('/near_me')
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all() #where Library.location == xxx
    return LibrarySchema(many=True).dump(libraries)





def register():
    library_info = librarySchema.load(request.json)

    library = library(
        email=library_info['email'],
        password #import bcrypt
        name=library_info.get
    )


    #get new library to db
    #confirm successful add 

#create register library route




