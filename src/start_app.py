"""

"""
# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from threading import Thread
import time

from logic.logging_handler import setup_graylog

from flask_definitions import *
import endpoints.unknown
import endpoints.user_handeling
import endpoints.general
import endpoints.logging


# ------------------------------------------------------- #
# functions
# ------------------------------------------------------- #


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    try:
        t = Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print('Received keyboard interrupt, quitting threads.')
        graylog_logger(level="info", handler="api", message={"event": "api stopped."})


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #


# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
setup_graylog(use_graylog, graylog_server)
keep_alive()
