#check imports
from flask import Blueprint, request
from setup import db
from flask_jwt_extended import jwt_required
from models.membership import MembershipSchema, Membership
from auth import authorise

memberships_bp = Blueprint('memberships', __name__, url_prefix='/memberships')


#get all memberships (of one user)
@memberships_bp.route('/')
#@jwt_required()
def all_memberships():
    #select * from libraries schema
    stmt = db.select(
        MembershipSchema
        )
    memberships = db.session.scalars(stmt).all()
    return MembershipSchema(many=True).dump(memberships)


#get one membership
@memberships_bp.route('/<int:id>')
@jwt_required()
def one_membership(id):
    stmt = db.select(Membership).filter_by(id=id)
    membership = db.session.scalar(stmt)
    if membership:
        return MembershipSchema().dump(membership)
    else:
        return {'error': 'Membership details not found'}, 404

#update one membership
@memberships_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_membership(id):
    membership_info = MembershipSchema().load(request.json)
    stmt = db.select(Membership).filter_by(id=id)
    membership = db.session.scalar(stmt)
    if membership:
        authorise(membership.user_id)
        membership.membership_number = membership_info.get('number', membership.membership_number)
        db.session.commit()
        return MembershipSchema().dump(membership)
    else:
        return {'error': 'Invalid membership update'}, 404

