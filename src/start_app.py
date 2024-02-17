"""

"""
# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from threading import Thread
import time
from waitress import serve

from flask_definitions import *
import endpoints.unknown
import endpoints.user_handeling
import endpoints.general
import endpoints.logging
import endpoints.web
import endpoints.matchmaking


# ------------------------------------------------------- #
# functions
# ------------------------------------------------------- #


def run():
    serve(app, host='0.0.0.0', port=8080)


def keep_alive():
    try:
        if dev_env == "true":
            logger.graylog_logger(level="info", handler="api", message={"event": "DEV api started."})
        else:
            logger.graylog_logger(level="info", handler="api", message={"event": "api started."})
        t = Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print('Received keyboard interrupt, quitting threads.')
        logger.graylog_logger(level="info", handler="api", message={"event": "api stopped."})


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #


# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
logger.setup_graylog(use_graylog, graylog_server)
mongo.setup(mongo_host, mongo_db, mongo_collection)
session_manager.setup()
keep_alive()
