from flask import jsonify
from log.log_config import setup_logger

logger = setup_logger("Error Handlers")
def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(error):
        logger.warning("ERROR HANDLER 400 GoT Called : BAD REQUEST")
        return jsonify({"message": "bad request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        logger.warning("ERROR HANDLER 404 GoT Called :NOT FOUND")
        return jsonify({"message": "not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.warning("ERROR HANDLER 500 GoT Called :EXCEPTION")
        return jsonify({"message": "wrong"}), 500
