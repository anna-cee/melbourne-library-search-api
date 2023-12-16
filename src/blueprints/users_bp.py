from flask_jwt_extended import create_access_token, jwt_required
from auth import authorise 
from flask import Blueprint, request
from models.user import User, UserSchema
from setup import bcrypt, db
from datetime import timedelta


#create blueprint

users_bp = Blueprint('users', __name__, url_prefix='/users')

#register or create user
@users_bp.route('/register', methods=['POST'])
@jwt_required
def register():
    authorise()
    user_info = UserSchema.load(request.json)

    user = User(
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('uft8'),
        name=user_info.get('name'),
    )
    
    

#     #get new user to db
    db.session.add(user)
    db.session.commit()

#     #confirm successful add 
    return UserSchema(exclude=['password']).dump(user), 201





#create login user route
@users_bp.route('/login', methods=['POST'])
def login():
    user_info = UserSchema.load(request.json)
    stmt = db.select(User).where(User.email == user_info['email'])
    user = db.session.scalar(stmt)
#password check
    if user and bcrypt.check_password_hash(user.passowrd, user_info['password']):
        #add access token
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
# add access token here

        return {
             'token': token,
             'user': UserSchema(exclude='password').dump(user)
        }
# #create a get user route - for who? admin?
