import datetime
import logging
logger = logging.getLogger(__name__)


def get_time():
    try:
        current_datetime = datetime.datetime.now()
        current_timestamp = int(current_datetime.timestamp())

        duration = 86400
        expiration_timestamp = current_timestamp + duration

        return current_timestamp, expiration_timestamp
    except Exception as e:
        logger.error("Error in time_handler -> " + str(e))
        return None, None
