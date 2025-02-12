from flask import Flask
from Contoller.routes import init_routes  # Import your routes
from error_handlers import register_error_handlers  # Import the error handler module
from log.log_config import setup_logger


def create_app():
    app = Flask(__name__)
    # Register the error handlers
    register_error_handlers(app)

    # setting up logger
    logger = setup_logger("app")
    logger.info("Flask application started")

    # Initialize routes
    init_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


