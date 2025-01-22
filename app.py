from flask import Flask
from Contoller.routes import *  # Import all routes from Contoller/routes.py

def init_app():
    app = Flask(__name__)
    init_routes(app)

    @app.before_first_request
    def init_db():
        pass

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        pass
    return app
if __name__ == '__main__':
    application = init_app()
    application.run(debug=True)
