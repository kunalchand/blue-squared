from flask import jsonify
from Service.logic import RecordService
from log.log_config import setup_logger

record_service = RecordService()

logger = setup_logger("Routes")

def init_routes(app):
    @app.route('/get_records/<int:id>', methods=['GET'])
    def get_records_single_id(id):
        try:

            records = record_service.get_records_single_id(id)
            logger.info(f"Fetch records based on one ID {id}")

            if records['table1'] is None and records['table2'] is None:
                return jsonify({"message": "Record not found in both tables"}), 200

            logger.info("Both table1 and table2 have no records")

            # Return the response with records from both tables (if they exist)
            logger.info("returning the records with 200 OK code")
            return jsonify(records), 200

        except Exception as e:
            # Return error if something goes wrong

            return jsonify({"message": str(e)}), 500


    @app.route('/get_records/<int:id1>/<int:id2>', methods=['GET'])
    def get_records(id1, id2):
        try:
            # Fetch records based on two different IDs
            records = record_service.get_records(id1, id2)
            logger.info(f"Fetch records based on Two IDs {id1},{id2}")

            # If both table1 and table2 have no records, return a not found response
            if records['table1'] is None and records['table2'] is None:
                return jsonify({"message": "Record not found in both tables"}), 200
            logger.info("Both table1 and table2 have no records")

            # Return the response with records from both tables (if they exist)
            logger.info("returning the records with 200 OK code")

            return jsonify(records), 200


        except Exception as e:
            # Return error if something goes wrong
            return jsonify({"message": str(e)}), 500
