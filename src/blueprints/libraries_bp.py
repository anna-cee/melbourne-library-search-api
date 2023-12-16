from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.library import LibrarySchema, Library


#create blueprint

librarys_bp = Blueprint('librarys', __name__)


#get all libraries
@librarys_bp.route('/')
@jwt_required()
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all()
    return LibrarySchema(many=True).dump(libraries)


#get libraries close to user locaiton - libraries/near_me
@librarys_bp.route('/near_me')
@jwt_required()
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalars(stmt).all() #where Library.location == xxx
    return LibrarySchema(many=True).dump(libraries)









