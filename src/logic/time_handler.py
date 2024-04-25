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


def get_date_and_time():
    try:
        current_time = datetime.datetime.utcnow()
        formatted_time = current_time.strftime('%a, %d %b %Y %H:%M:%S MEZ')
        return formatted_time
    except Exception as e:
        logger.error("Error in time_handler -> " + str(e))
        return None


def get_lifetime(challenge_type):
    try:
        # "lifetime":{
        #             "creationTime":"2019-11-25T02:17:22.484Z",
        #           "expirationTime":"2019-11-25T17:59:59.000Z"
        #          }
        if challenge_type == "Daily":
            creation_time = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='milliseconds')
            expiration_time = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0).isoformat(timespec='milliseconds')
        elif challenge_type == "Weekly":
            creation_time = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='milliseconds')
            expiration_time = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)).replace(hour=23, minute=59, second=59, microsecond=0).isoformat(timespec='milliseconds')
        else:
            return None
        return creation_time, expiration_time
    except Exception as e:
        logger.error("Error in time_handler -> " + str(e))
        return None
