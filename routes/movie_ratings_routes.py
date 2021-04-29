from flask import Blueprint, jsonify, make_response, request
from database import session
from models import MovieRating

movie_ratings_router = Blueprint('movie_ratings_router', __name__, url_prefix='/api/v1/ratings/')


@movie_ratings_router.route('/', methods=["GET"])
def get_all_movies():
    ratings = session.query(MovieRating).all()

    result = [
        {
            'id': rating.id,
            'movie_id': rating.movie_id,
            # 'movie': rating.get_movie_by_id(),
            'user_id': rating.user_id,
            'user': rating.get_user_by_id()
        }
        for rating in ratings]

    return make_response(jsonify({'ratings': result, 'status': 200}), 200)


@movie_ratings_router.route('/', methods=["POST"])
def create_movie():
    data = request.get_json()

    if data is None:
        return make_response(jsonify({'message': 'error submitting rating, body is required', 'status': 500}), 500)

    rating = MovieRating(movie_id=data['movie_id'], user_id=data['user_id'], rating=data['rating'])

    session.add(rating)

    try:
        session.commit()
    except Exception as e:
        return make_response(jsonify({'message': 'error submitting rating, {}'.format(str(e)), 'status': 500}), 500)

    return make_response(jsonify({'message': 'rating submitted', 'status': 201}), 201)
