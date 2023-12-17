#check imports
from flask import Blueprint, request
from setup import db
from flask_jwt_extended import jwt_required
from models.membership import MembershipSchema, Membership
from auth import authorise

memberships_bp = Blueprint('memberships', __name__, url_prefix='/memberships')


#get all memberships (of one user)
@memberships_bp.route('/all')
#@jwt_required()
def all_memberships():
    #select * from libraries schema
    stmt = db.select(
        Membership
        )
    memberships = db.session.scalars(stmt).all()
    return MembershipSchema(many=True).dump(memberships)


#update one membership
@memberships_bp.route('/update/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_membership(id):
    membership_info = MembershipSchema().load(request.json)
    stmt = db.select(Membership).filter_by(id=id)
    membership = db.session.scalar(stmt)
    if membership:
        authorise(membership.user_id)
        membership.number = membership_info.get('number', membership.number)
        db.session.commit()
        return MembershipSchema().dump(membership)
    else:
        return {'error': 'Invalid membership update'}, 404


#Delete a membership
    
@memberships_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_membership(id):
    stmt = db.select(Membership).filter_by(id=id).where(Membership.id == membership.number)
    membership = db.session.scalar(stmt)
    if membership:
        authorise(membership.user_id)
        db.session.delete(membership)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Membership not deleted'}, 404

