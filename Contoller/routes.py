from flask import jsonify
from View.view import format_response
from Service.logic import RecordService,Records
from log.log_config import setup_logger

logger = setup_logger("routes")

record_service = RecordService(Records)


def init_routes(app):
    @app.route('/get_records/<id>', methods=['GET'])
    def get_records_single_id(id):
        if not id.isdigit():
            logger.warning(f"Invalid ID {id} provided, returning 400 Bad Request.")
            return jsonify({"message": "Invalid ID format. IDs should be an integer."}), 400

        records = record_service.get_records_single_id(id)
        return format_response(records)

    @app.route('/get_records/<id1>/<id2>', methods=['GET'])
    def get_records(id1, id2):
        if not id1.isdigit() or not id2.isdigit():  # If it's not a number, raise a 400 error
            logger.warning(f"Invalid ID {id1} and {id2} provided, returning 400 Bad Request.")
            return jsonify({"message": "Invalid ID format. IDs should be an integer."}), 400

        records = record_service.get_records(id1, id2)
        return format_response(records)
