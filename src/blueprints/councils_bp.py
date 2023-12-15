

#create blueprint

councils_bp = Blueprint('councils', __name__)

@councils_bp.route('/register', methods=['POST'])

def register():
    council_info = councilSchema.load(request.json)

    council = council(
        email=council_info['email'],
        password #import bcrypt
        name=council_info.get
    )


    #get new council to db
    #confirm successful add 

#create register council route




#create login council route
@councils_bp.route('/login', methods=['POST'])

def_login():
council_info = councilSchema.load(request.json)
stmt = db.select(council).where(council.email == council_info['email'])
council = db.session.scalar(stmt)
#password check
#add access token here



#create a get council route - for who? admin?



