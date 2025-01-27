# error_handlers.py
from flask import jsonify

def register_error_handlers(app):

    # Handle 400 Bad Request errors
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"message": "IDs must be 1, above 1"}), 200

    # Handle 404 Not Found errors
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"message": "IDs must be 1,above 1"}), 200
