# config/config.py

import os


def get_db_url():
    return os.getenv('DB_URL', 'postgresql://postgres:Postgres%401234@localhost:5433/TrainingDB')