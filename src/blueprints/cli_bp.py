
#check imports
from flask import Blueprint
from app import db, bcrypt
from models.user import User


#connect to blue prints
db_commands = Blueprint('db', __name__)

#table create function
@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created all tables')

#table seed fucntion
    #add table data here
@db_commands.cli.command('seed')
def db_seed():
    #add users
    users =[
        User(
            email='mary@email.com',
            name='Mary Reader'
            password = 'dddd',
            is_admint = True,
            suburb = 'Fitzroy'
        ),

        User(
            email='jaques@email.com',
            name='Jacques de Livres', 
            password = 'rrrr',
            is_admint = True,
            suburb = 'Coburg'

        ),

        User(
            email='kendall@email.com',
            name='Kendall Nonfiction',
            password = 'dddd',
            is_admint = True,
            suburb = 'East Melbourne'

        ),

        User(
            email='alex@email.com',
            name= 'Alex Genre',
            password = 'dddd',
            is_admint = True,
            suburb = 'Fitzroy'

        ),
    ]


    #db.session.add(users)
    #db.session.commit()

#Councils
    councils = [
        Council(
            name="City of Melbourne",
            email="citymelbcouncil@email.com",
        ),
        Council(
            name="Yarra",
            email="yarracouncil@email.com"
        ),
        Council(
            name="Merri-bek",
            email="merri-bekcouncil@email.com"
        ),
        Council(
            name="Darebin",
            email="darebincouncil@email.com"
        ),

        Council(
            name="Banyule",
            email="banyulecouncil@email.com"
        ),
        Council(
            name="Boroondara",
            email="boroondaracouncil@email.com"
        ),

    ]

    #db.session.add(councils)
    #db.session.commit()



#Libraries
    librarys = [
        Library(
            name= 'City Library',
            suburb='Melbourne',
            council='City of Melbourne'
        ),
        Library(
            name= 'East Melbourne Library',
            suburb='East Melbourne',
            council='City of Melbourne'
        ),
        Library(
            name= 'Kathleen Syme Library and Community Centre',
            suburb='Carlton',
            council='City of Melbourne'
        ),
        Library(
            name= 'Library at The Dock',
            suburb='Docklands',
            council='City of Melbourne'
        ),
        Library(
            name= 'narrm ngarrgu Library and Family Services',
            suburb='Melbourne',
            council='City of Melbourne'
        )
        Library(
            name= 'North Melbourne Library',
            suburb='North Melbourne',
            council='City of Melbourne'
        )
        Library(
            name= 'Southbank Library',
            suburb='Southbank',
            council='City of Melbourne'
        ),
        Library(
            name='Ashburton Library',
            suburb='154 High Street, Ashburton VIC 3147',
            council='Boroondara'
        ),
        Library(
            name='Balwyn Library',
            suburb= '336 Whitehorse Road Balwyn VIC 3103',
            council='Boroondara'
        ),
        Library(
            name='Camberwell Library',
            suburb='340 Camberwell Road, Camberwell VIC 3124',
            council='Boroondara'
        ),
        Library(
            name='Greythorn Library Lounge',
            suburb='2 Centre Way, Balwyn North VIC 3104',
            council='Boroondara'
        ),
        Library(
            name='Hawthorn Library',
            suburb='584 Glenferrie Road, Hawthorn VIC 3122',
            council='Boroondara'
        ),
        Library(
            name='Kew Library',
            suburb='Corner Cotham Road and Civic Drive, Kew VIC 3101',
            council='Boroondara'
        ),
        Libarary(
            name='Bargoonga Nganjin, North Fitzroy Library',
            suburb='182 St Georges Road, North Fitzroy',
            council='Yarra'
        ),
        Library(
            name='Carlton Library',
            suburb='667 Rathdowne Street, North Carlton'
            council='Yarra'
        ),
        Library(
            name='Collingwood Library',
            suburb='11 Stanton Street, Abbotsford',
            council='Yarra'
        ),
        Library(
            name='Fitzroy Library',
            suburb='128 Moor Street, Fitzroy',
            council='Yarra'
        ),
        Library(
            name='Richmond Library',
            suburb='415 Church Street, Richmond',
            council='Yarra'
        ),
        Library(
            name='Brunswick Library',
            suburb='Corner Sydney Road and Dawson Street, Brunswick',
            council='Merri-bek'
        ),
        Library(
            name='Campbell Turnbull Library',
            suburb='220 Melville Road, Brunswick West',
            council='Merri-bek'
        ),
        Library(
            name='Coburg Library',
            suburb='Corner Victoria and Louisa Streets, Coburg',
            council='Merri-bek'
        ),
        Library(
            name='Fawkner library',
            suburb='77 Jukes Road, Fawkner',
            council='Merri-bek'
        ),
        Library(
            name='Glenroy library',
            suburb='50 Wheatsheaf Rd, Glenroy',
            council='Merri-bek'
        ),
        Library(
            name='Fairfield Library',
            suburb='121 Station Street, Fairfield',
            council='Darebin'
        ),
        Library(
            name='Northcote Library',
            suburb='32-38 Separation Street, Northcote',
            council='Darebin'
        ),
        Library(
            name='Preston Library',
            suburb='266 Gower Street, Preston',
            council='Darebin'
        ),
        Library(
            name='Reservoir Library',
            suburb='23 Edwardes Street, Reservoir',
            council='Darebin'
        ),
        Library(
            name='Watsonia Library',
            suburb='4 Ibbottson Street, Watsonia, 3087',
            council='Banyule'
        ),
        Library(
            name='Rosanna Library',
            suburb='72 Turnham Ave, Rosanna, 3084'
            council='Banyule'
        ),
        Library(
            name='Ivanhoe Library & Cultural Hub'
            suburb='255 Upper Heidelberg Road, Ivanhoe, 3079'
            council='Banyule',
        ),

    ]

    #db.session.add(librarys)
    #db.session.commit()

#Memberships

    memberships = [
        Membership(
            number='1456372'
            user_id='ss1'
            council='Banyule'
        ),
        Membership(
            number='200003483920'
            user_id='s1'
            council="City of Melbourne"
        ),

        Membership(
            number='1289234794'
            user_id='s2'
            council="Yarra
        ),
        Membership(
            number='1643297'
            user_id='s2'
            council="Merri-bek"
        ),
        Membership(
            number='20093477834297'
            user_id='s3'
            council="City of Melbourne"
        ),
        Membership(
            number='1238803408354'
            user_id='s3'
            council="Darebin"
        ),
        Membership(
            number='5473893'
            user_id='s4'
            council="Boroondara"
        ),
        Membership(
            number='123234'
            user_id='sss'
            council="Banyule"
        ),
        
    ]
    #db.session.add(memberships)
    #db.session.commit()


#Locations
    locations = [
        Location(
            name='Melbourne',
            longitude=
            latitutde=
        ),
        Location(
            name='East Melbourne',
            longitude=
            latitutde=
        ),
        Location(
            name='North Melbourne',
            longitude=
            latitutde=
        ),
        Location(
            name='Docklands',
            longitude=
            latitutde=
        ),
        Location(
            name='Fitzroy',
            longitude=
            latitutde=
        ),
        Location(
            name='North Fitzroy',
            longitude=
            latitutde=
        ),
        Location(
            name='Abbotsford',
            longitude=
            latitutde=
        ),
        Location(
            name='Carlton',
            longitude=
            latitutde=
        ),
        Location(
            name='Collingwood',
            longitude=
            latitutde=
        ),
        Location(
            name='Brunswick',
            longitude=
            latitutde=
        ),
        Location(
            name='Brunswick East',
            longitude=
            latitutde=
        ),

        Location(
            name='Coburg',
            longitude=
            latitutde=
        ),
        Location(
            name='Reservoir',
            longitude=
            latitutde=
        ),
        Location(
            name='Northcote',
            longitude=
            latitutde=
        ),
        Location(
            name='Thornbury',
            longitude=
            latitutde=
        ),
        Location(
            name='Preston',
            longitude=
            latitutde=
        ),
        Location(
            name='Fairfield',
            longitude=
            latitutde=
        ),Location(
            name='Glenroy',
            longitude=
            latitutde=
        ),Location(
            name='Fawkner',
            longitude=
            latitutde=
        ),Location(
            name='Rosanna',
            longitude=
            latitutde=
        ),Location(
            name='Watsonia',
            longitude=
            latitutde=
        ),
        Location(
            name='Brunswick West',
            longitude=
            latitutde=
        ),
        Location(
            name='Richmond',
            longitude=
            latitutde=
        ),


    ]

    #db.session.add(locations)
    #db.session.commit()



#Holdings
    holdings = [
        Holding(
            ISBN='9780399226908',
            title='The Very Hungry Catepillar',
            author='Eric Carle'
        ),
        Holding(
            ISBN='9781787633735',
            title='Better Off Dead',
            author='Lee Child'
        ),
        Holding(
            ISBN='9780241444184',
            title='Scandal of the century and other writings',
            author='Gabriel García Márquez'
        ),
        Holding(
            ISBN='9781338893076',
            title='The Official Harry Potter Cookbook',
            author='Joanna Farrow'
        ),
        
    ]

    #db.session.add(holdings)
    #db.session.commit()

