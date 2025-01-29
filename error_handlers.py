# error_handlers.py
from flask import jsonify

def register_error_handlers(app):


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"message": "IDs must be positive numbers "}), 200


    @app.errorhandler(500)
    def not_found(error):
        return jsonify({"message": "wrong"}), 500
