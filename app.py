from flask import Flask
from flask_cors import CORS
from database import Base, engine
import routes

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app)
# Register routes blueprints
app.register_blueprint(routes.movies_router)
app.register_blueprint(routes.genres_router)
app.register_blueprint(routes.users_router)
app.register_blueprint(routes.movie_ratings_router)

if __name__ == '__main__':
    app.run()
