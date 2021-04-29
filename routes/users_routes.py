from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash

from database import session
from models import User

users_router = Blueprint('users_routes', __name__, url_prefix="/api/v1/users/")


@users_router.route('/', methods=['GET'])
def get_all_users():
    users = session.query(User).all()

    result = [
        {
            'id': user.id,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'username': user.username
        }
        for user in users]

    return make_response(jsonify({'users': result, 'status': 200}), 200)


@users_router.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    if data is None:
        return make_response(jsonify({'message': 'error creating user, body is required', 'status': 500}), 500)

    password_hash = data['password']
    password_hash = generate_password_hash(password_hash)
    new_user = User(firstname=data['firstname'], lastname=data['lastname'], username=data['username'],
                    password_hash=password_hash)

    session.add(new_user)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'message': 'error creating user, {}'.format(str(e)), 'status': 500}), 500)

    return make_response(jsonify({'message': 'user created', 'status': 201}), 201)
