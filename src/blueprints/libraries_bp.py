from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.library import LibrarySchema, Library


#create blueprint

libraries_bp = Blueprint('libraries', __name__, url_prefix='/libraries')


#get all libraries
@libraries_bp.route('/all')
#@jwt_required()
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all()
    return LibrarySchema(many=True).dump(libraries)


#get libraries close to user locaiton - libraries/near_me
@libraries_bp.route('/near_me')
#@jwt_required()
def libraries_near():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all() #where Library.location == xxx
    return LibrarySchema(many=True).dump(libraries)









