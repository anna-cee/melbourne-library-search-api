from flask_jwt_extended import create_access_token, jwt_required
from auth import authorise 
from flask import Blueprint, request
from models.council import Council, CouncilSchema
from setup import bcrypt, db
from datetime import timedelta


#create blueprint

councils_bp = Blueprint('councils', __name__, url_prefix='/councils')

#register or create council
@councils_bp.route('/register', methods=['POST'])
#@jwt_required
def register():
    authorise()
    council_info = CouncilSchema.load(request.json)

    council = Council(
        email=council_info['email'],
        password=bcrypt.generate_password_hash(council_info['password']).decode('uft8'),
        name=council_info.get('name'),
    )
    
    

#     #get new council to db
    db.session.add(council)
    db.session.commit()

#     #confirm successful add 
    return CouncilSchema(exclude=['password']).dump(council), 201





#create login council route
@councils_bp.route('/login', methods=['POST'])
def login():
    council_info = CouncilSchema.load(request.json)
    stmt = db.select(Council).where(Council.email == council_info['email'])
    council = db.session.scalar(stmt)
#password check
    if council and bcrypt.check_password_hash(council.passowrd, council_info['password']):
        #add access token
        token = create_access_token(identity=council.id, expires_delta=timedelta(hours=2))
# add access token here

        return {
             'token': token,
             'council': CouncilSchema(exclude='password').dump(council)
        }
# #create a get council route - for who? admin?
