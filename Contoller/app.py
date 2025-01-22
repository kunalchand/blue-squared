from flask import Flask, jsonify
from Service.logic import RecordService

app = Flask(__name__)

# Define the database connection URL
db_url = 'postgresql://postgres:Postgres%401234@localhost:5433/TrainingDB'

# Initialize the RecordService with the DB URL
record_service = RecordService(db_url)

@app.route('/get_records/<int:id>', methods=['GET'])
def get_records(id):
    try:
        records = record_service.get_records(id)
        if not records['table1'] and not records['table2']:
            return jsonify({"message": "Record not found in both tables"}), 404
        return jsonify(records), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.before_first_request
def init_db():
    # Add any necessary initialization before the first request (like opening a DB connection)
    pass

@app.teardown_appcontext
def shutdown_session(exception=None):
    # Close the session when the app context is destroyed
    record_service.close()

if __name__ == '__main__':
    app.run(debug=True)
