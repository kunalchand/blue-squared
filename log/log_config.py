import logging
import os

# Create log directory if it doesn't exist
log_directory = 'log'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Define the log file path
log_file_path = os.path.join(log_directory, 'app_log.log')

# Set up the logging configuration
def setup_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # Create a file handler that logs messages to the specified file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)


    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - Line %(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Set formatter for handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
