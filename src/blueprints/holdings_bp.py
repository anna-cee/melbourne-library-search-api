from flask_jwt_extended import create_access_token, jwt_required
from auth import authorise 
from flask import Blueprint, request
from models.holding import Holding, HoldingSchema
from setup import bcrypt, db

#find a holding
holdings_bp = Blueprint('holdings', __name__, url_prefix='/holdings')

@holdings_bp.route('/<int:id>', methods=['GET', 'POST'])
@jwt_required()
def find_title(id):
    stmt = db.select(Holding).filter_by(id=id).where(Holding.title == id)
    holding = db.session.scalar(stmt)
    if holding:
         return HoldingSchema().dump(holding)
    else:
         return {'error': 'Title not found'}, 404
    
@holdings_bp.route('/<int:id>', methods=['GET', 'POST'])
@jwt_required()
def find_author(id):
    stmt = db.select(Holding).filter_by(id=id).where(Holding.author == id)
    holding = db.session.scalar(stmt)
    if holding:
         return HoldingSchema().dump(holding)
    else:
         return {'error': 'Title not found'}, 404
     