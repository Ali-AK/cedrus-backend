from flask import Blueprint, request, make_response, jsonify
from models import Genre
from database import session

genres_router = Blueprint('genres_router', __name__, url_prefix="/api/v1/genres/")


@genres_router.route('/', methods=['GET'])
def get_all_genres():
    genres = session.query(Genre).all()

    result = [
        {
            'id': genre.id,
            'name': genre.name
        }
        for genre in genres]

    return make_response(jsonify({'genres': result, 'status': 200}), 200)


@genres_router.route('/', methods=['POST'])
def create_genre():
    data = request.get_json()

    new_genre = Genre(name=data['name'])
    session.add(new_genre)
    try:
        session.commit()
    except Exception as e:
        return e

    return make_response(jsonify({'genre': str(new_genre), 'status': 201}), 201)


@genres_router.route('/populate', methods=["POST"])
def populate_genres():
    genres = request.json

    if genres is None:
        return make_response(jsonify({'message': 'error populating genres, body is required', 'status': 500}), 500)

    for genre in genres:
        new_genre = Genre(name=genre['name'])
        session.add(new_genre)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'message': 'error populating genres, {}'.format(str(e)), 'status': 500}), 500)

    return make_response(jsonify({'message': 'genres populated', 'status': 201}), 201)
