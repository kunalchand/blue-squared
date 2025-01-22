# config/config.py

import os

# Function to get DB URL, can have logic for dynamic values
def get_db_url():
    # You can add any logic to determine the DB URL here (e.g., based on environment variables)
    return os.getenv('DB_URL', 'postgresql://postgres:Postgres%401234@localhost:5433/TrainingDB')
