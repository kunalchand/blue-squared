from flask import jsonify
from log.log_config import setup_logger


def format_response(data):
    logger = setup_logger("View")
    logger.info(f"View is initiated")
    return jsonify(data)

