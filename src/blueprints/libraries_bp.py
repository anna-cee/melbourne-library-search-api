from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.library import LibrarySchema, Library


#create blueprint

libraries_bp = Blueprint('libraries', __name__, url_prefix='/libraries')


#get all libraries
@libraries_bp.route('/')
#@jwt_required()
def all_libraries():
    #select * from libraries schema
    stmt = db.select(
        Library
        )
    libraries = db.session.scalar(stmt).all()
    return LibrarySchema(many=True).dump(libraries)











