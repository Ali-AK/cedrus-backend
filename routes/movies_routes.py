from flask import Blueprint, jsonify, make_response, request
from database import session
from models import Movie

movies_router = Blueprint('movies_router', __name__, url_prefix='/api/v1/movies/')


@movies_router.route('/', methods=["GET"])
def get_all_movies():
    movies = session.query(Movie).all()

    result = [
        {
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'genre': movie.get_genre_by_id(),
            'rating': movie.get_rating_by_id()
        }
        for movie in movies]

    return make_response(jsonify({'movies': result, 'status': 200}), 200)


@movies_router.route('/', methods=["POST"])
def create_movie():
    data = request.get_json()

    if data is None:
        return make_response(jsonify({'message': 'error creating movie, body is required', 'status': 500}), 500)

    movie = Movie(title=data['title'], description=data['description'], genre_id=data['genre_id'])

    session.add(movie)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'message': 'error creating movie, {}'.format(str(e)), 'status': 500}), 500)

    return make_response(jsonify({'message': 'movie created', 'status': 201}), 201)


@movies_router.route('/populate', methods=["POST"])
def populate_movies():
    movies = request.json

    if movies is None:
        return make_response(jsonify({'message': 'error populating movies, body is required', 'status': 500}), 500)

    for movie in movies:
        new_movie = Movie(title=movie['title'], description=movie['description'], genre_id=movie['genre_id'])
        session.add(new_movie)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'message': 'error populating movies, {}'.format(str(e)), 'status': 500}), 500)

    return make_response(jsonify({'message': 'movies populated', 'status': 201}), 201)


@movies_router.route('/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):

    movie = session.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        return make_response(jsonify({'response': 'Movie not found', 'status': 404}))

    session.delete(movie)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'Error': 'Movie was not deleted', 'status': 500}), 500)

    return make_response(jsonify({'response': 'Movie has been deleted', 'status': 200}), 200)