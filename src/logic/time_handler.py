import datetime


def get_time():
    current_datetime = datetime.datetime.now()
    current_timestamp = int(current_datetime.timestamp())

    duration = 86400
    expiration_timestamp = current_timestamp + duration

    return current_timestamp, expiration_timestamp
