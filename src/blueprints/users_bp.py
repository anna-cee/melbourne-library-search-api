#check imports

#connect Blueprint


#define routes!



#create blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/register', methods=['POST'])

def register():
    user_info = UserSchema.load(request.json)

    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash()'#import bcrypt
        name=user_info.get
    )


    #get new user to db
    #confirm successful add 

#create register user route




#create login user route
@users_bp.route('/login', methods=['POST'])

def_login():
user_info = UserSchema.load(request.json)
stmt = db.select(User).where(User.email == user_info['email'])
user = db.session.scalar(stmt)
#password check
#add access token here



#create a get user route - for who? admin?
