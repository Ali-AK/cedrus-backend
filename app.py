from flask import Flask
from database import Base, engine
import routes

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
# Register routes blueprints
app.register_blueprint(routes.movies_router)
app.register_blueprint(routes.genres_router)
app.register_blueprint(routes.users_router)

if __name__ == '__main__':
    app.run()
