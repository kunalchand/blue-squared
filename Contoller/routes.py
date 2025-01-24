from flask import jsonify
from Service.logic import RecordService

# Initialize the RecordService
record_service = RecordService()

def init_routes(app):
    @app.route('/get_records/<int:id>', methods=['GET'])
    def get_records(id):
        try:
            records = record_service.get_records(id)
            if not records['table1'] and not records['table2']:
                return jsonify({"message": "Record not found in both tables"}), 200
            return jsonify(records), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 500
