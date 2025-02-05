import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


class ErrorHandler:
    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_info(message):
        logging.info(message)


error_handler = ErrorHandler()
