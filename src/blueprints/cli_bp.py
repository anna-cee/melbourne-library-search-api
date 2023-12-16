
#check imports
from flask import Blueprint
from setup import db
from setup import bcrypt
from models.user import User
from models.council import Council
from models.holding import Holding
from models.membership import Membership
from models.library import Library
from models.location import Location
from datetime import date



#connect to blue prints
db_commands = Blueprint('db', __name__)

#table create 
@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created all tables')

#table seed function
    #add table data here
@db_commands.cli.command('seed')
def db_seed():
    #add users
    users =[
        User(
            email='mary@email.com',
            name='Mary Reader',
            password=bcrypt.generate_password_hash('MaryReadsBooks').decode('utf8'),
            is_admin=False,
            location='Fitzroy',
        ),

        User(
            email='jaques@email.com',
            name='Jacques de Livres', 
            password=bcrypt.generate_password_hash('JacquesAimesDesLivres').decode('utf8'),
            is_admin=False,
            location='Coburg',

        ),

        User(
            email='kendall@email.com',
            name='Kendall Nonfiction',
            password=bcrypt.generate_password_hash('KendallLovesHistory').decode('utf8'),
            is_admin=False,
            location='East Melbourne',
        ),

        User(
            email='alex@email.com',
            name= 'Alex Genre',
            password = bcrypt.generate_password_hash('AlexLoansHorror').decode('utf8'),
            is_admint = True,
            location = 'Fitzroy',

        ),
    ]


    db.session.add(users)
    db.session.commit()

#Councils
    councils = [
        Council(
            name="City of Melbourne",
            email="citymelbcouncil@email.com",
        ),
        Council(
            name="Yarra",
            email="yarracouncil@email.com",
        ),
        Council(
            name="Merri-bek",
            email="merri-bekcouncil@email.com",
        ),
        Council(
            name="Darebin",
            email="darebincouncil@email.com",
        ),

        Council(
            name="Banyule",
            email="banyulecouncil@email.com",
        ),
        Council(
            name="Boroondara",
            email="boroondaracouncil@email.com",
        ),

    ]

    db.session.add(councils)
    db.session.commit()



#Libraries
    libraries = [
        Library(
            name= 'City Library',
            location='Melbourne',
            #council='City of Melbourne',
        ),
        Library(
            name= 'East Melbourne Library',
            location='East Melbourne',
           # council='City of Melbourne'
        ),
        Library(
            name= 'Kathleen Syme Library and Community Centre',
            location='Carlton',
            #council='City of Melbourne',
        ),
        Library(
            name= 'Library at The Dock',
            location='Docklands',
            #council='City of Melbourne',
        ),
        Library(
            name= 'narrm ngarrgu Library and Family Services',
            location='Melbourne',
            #council='City of Melbourne',
        ),
        Library(
            name= 'North Melbourne Library',
            location='North Melbourne',
            #council='City of Melbourne',
        ),
        Library(
            name= 'Southbank Library',
            location='Southbank',
            #council='City of Melbourne',
        ),
        Library(
            name='Ashburton Library',
            location='154 High Street, Ashburton VIC 3147',
            #council='Boroondara',
        ),
        Library(
            name='Balwyn Library',
            location= '336 Whitehorse Road Balwyn VIC 3103',
            #council='Boroondara',
        ),
        Library(
            name='Camberwell Library',
            location='340 Camberwell Road, Camberwell VIC 3124',
            #council='Boroondara',
        ),
        Library(
            name='Greythorn Library Lounge',
            location='2 Centre Way, Balwyn North VIC 3104',
            #council='Boroondara',
        ),
        Library(
            name='Hawthorn Library',
            location='584 Glenferrie Road, Hawthorn VIC 3122',
            #council='Boroondara',
        ),
        Library(
            name='Kew Library',
            location='Corner Cotham Road and Civic Drive, Kew VIC 3101',
            #council='Boroondara',
        ),
        Library(
            name='Bargoonga Nganjin, North Fitzroy Library',
            location='182 St Georges Road, North Fitzroy',
            #council='Yarra',
        ),
        Library(
            name='Carlton Library',
            location='667 Rathdowne Street, North Carlton'
            #council='Yarra',
        ),
        Library(
            name='Collingwood Library',
            location='11 Stanton Street, Abbotsford',
            #council='Yarra',
        ),
        Library(
            name='Fitzroy Library',
            location='128 Moor Street, Fitzroy',
            #council='Yarra',
        ),
        Library(
            name='Richmond Library',
            location='415 Church Street, Richmond',
            #council='Yarra',
        ),
        Library(
            name='Brunswick Library',
            location='Corner Sydney Road and Dawson Street, Brunswick',
            #council='Merri-bek',
        ),
        Library(
            name='Campbell Turnbull Library',
            location='220 Melville Road, Brunswick West',
            #council='Merri-bek',
        ),
        Library(
            name='Coburg Library',
            location='Corner Victoria and Louisa Streets, Coburg',
            #council='Merri-bek',
        ),
        Library(
            name='Fawkner library',
            location='77 Jukes Road, Fawkner',
            #council='Merri-bek'
        ),
        Library(
            name='Glenroy library',
            location='50 Wheatsheaf Rd, Glenroy',
            #council='Merri-bek'
        ),
        Library(
            name='Fairfield Library',
            location='121 Station Street, Fairfield',
            #council='Darebin'
        ),
        Library(
            name='Northcote Library',
            location='32-38 Separation Street, Northcote',
            #council='Darebin'
        ),
        Library(
            name='Preston Library',
            location='266 Gower Street, Preston',
            #council='Darebin'
        ),
        Library(
            name='Reservoir Library',
            location='23 Edwardes Street, Reservoir',
            #council='Darebin'
        ),
        Library(
            name='Watsonia Library',
            location='4 Ibbottson Street, Watsonia, 3087',
            #council='Banyule'
        ),
        Library(
            name='Rosanna Library',
            location='72 Turnham Ave, Rosanna, 3084'
            #council='Banyule'
        ),
        Library(
            name='Ivanhoe Library & Cultural Hub',
            location='255 Upper Heidelberg Road, Ivanhoe, 3079'
            #council='Banyule',
        ),
    ]

    db.session.add(libraries)
    db.session.commit()

#Memberships

    memberships = [
        Membership(
            number='1456372',
            #user_id='ss1'
            #council='Banyule'
            #date_created=date,
        ),
        Membership(
            number='200003483920',
            #user_id='s1'
            #council="City of Melbourne"
        ),

        Membership(
            number='1289234794',
            #user_id='s2'
            #council="Yarra
        ),
        Membership(
            number='1643297',
            #user_id='s2'
            ##council="Merri-bek"
        ),
        Membership(
            number='20093477834297',
            #user_id='s3'
            #council="City of Melbourne"
        ),
        Membership(
            number='1238803408354',
            #user_id='s3'
            #council="Darebin"
        ),
        Membership(
            number='5473893',
            #user_id='s4'
            #council="Boroondara"
        ),
        Membership(
            number='123234',
            #user_id='sss'
            #council="Banyule"
        ),
    ]

    db.session.add(memberships)
    db.session.commit()


#Locations
    locations = [
        Location(
            name='Northcote',
           # latitutde=-37.772202, 
            #longitude=144.999405,
        ),
        Location(
            name='East Melbourne',
           # latitutde=-37.8103,
        
            #longitude=144.9835
        ),
        Location(
            name='North Melbourne',
           
        ),
        Location(
            name='Docklands',
            
        ),
        Location(
            name='Fitzroy',
           
        ),
        Location(
            name='North Fitzroy',
            #latitutde=
            #longitude=
        ),
        Location(
            name='Abbotsford',
            #latitutde=
          #  longitude=
        ),
        Location(
            name='Carlton',
           # latitutde=
            #longitude=
        ),
        Location(
            name='Collingwood',
            #latitutde=
            #longitude=
        ),
        Location(
            name='Brunswick',
            #latitutde=
            #longitude=
        ),
        Location(
            name='Brunswick East',
            #latitutde=
            #longitude=
        ),

        Location(
            name='Coburg',
            #latitutde=
            #longitude=
        ),
        Location(
            name='Reservoir',
            #latitutde=
            #longitude=
        ),
        Location(
            name='Northcote',
           # longitude=
            #latitutde=
        ),
        Location(
            name='Thornbury',
            #longitude=
         #   latitutde=
        ),
        Location(
            name='Preston',
          #  longitude=
           # latitutde=
        ),
        Location(
            name='Fairfield',
            #longitude=
            #latitutde=
        ),Location(
            name='Glenroy',
            #longitude=
            #latitutde=
        ),Location(
            name='Fawkner',
            #longitude=
            #latitutde=
        ),Location(
            name='Rosanna',
            #longitude=
            #latitutde=
        ),Location(
            name='Watsonia',
            #longitude=
            #latitutde=
        ),
        Location(
            name='Brunswick West',
            #longitude=
            #latitutde=
        ),
        Location(
            name='Richmond',
            #longitude=
            #latitutde=
        ),


    ]

    db.session.add(locations)
    db.session.commit()



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

    db.session.add(holdings)
    db.session.commit()

    print('database seeded')