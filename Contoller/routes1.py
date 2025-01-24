from flask import jsonify
from Service.logic1 import RecordService

record_service = RecordService()


def init_routes(app):
    @app.route('/get_records/<int:id1>/<int:id2>', methods=['GET'])
    def get_records(id1, id2):
        try:
            # Fetch records based on two different IDs
            records = record_service.get_records(id1, id2)
            # If both table1 and table2 have no records, return a not found response
            if records['table1'] is None and records['table2'] is None:
                return jsonify({"message": "Record not found in both tables"}), 200

            # Return the response with records from both tables (if they exist)
            return jsonify(records), 200
        except Exception as e:
            # Return error if something goes wrong
            return jsonify({"message": str(e)}), 500
