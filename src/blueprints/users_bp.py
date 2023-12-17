from flask_jwt_extended import create_access_token, jwt_required
from auth import authorise 
from flask import Blueprint, request
from models.user import User, UserSchema
from setup import bcrypt, db
from datetime import timedelta


#create blueprint #add URL prefix for all user routes
users_bp = Blueprint('users', __name__, url_prefix='/users')

#register or create new user
@users_bp.route('/register', methods=['POST'])
@jwt_required
def register():
    authorise()
    
    #Inputted post data parsed through json schema
    user_info = UserSchema(exclude=['id', 'is_admin']).load(request.json)

    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('uft8'),
        name=user_info.get('name'),
    )
    

   #commit new user post to db
    db.session.add(user)
    db.session.commit()

    #confirm successful add 
    return UserSchema(exclude=['password']).dump(user), 201





#user login route
@users_bp.route('/login', methods=['POST'])
def login():
    #jsonify login data through M/mallow schema
    user_info = UserSchema(exclude=['id', 'name', 'is_admin', 'location']).load(request.json)
    #confirm email match
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
    #password check
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        #add access token
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        #token back to client

        return {
             'token': token,
             'user': UserSchema(exclude='password').dump(user)
        }
    else:
        return{'error': 'Incorrect email or password. Please try again.'}, 401



@users_bp.route("/")
@jwt_required()
def all_users():
    authorise() # admin permissions
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    print(users)
    return UserSchema(many=True, exclude=["password"]).dump(users)