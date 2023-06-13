import logging
import graypy

my_logger = logging.getLogger('deathgarden_api')


def setup_graylog(use_graylog, graylog_server):
    if use_graylog:
        my_logger.setLevel(logging.DEBUG)
        handler = graypy.GELFUDPHandler(graylog_server, 12201)
        my_logger.addHandler(handler)
        my_logger.info({"level": "info", "handler": "api", "message": {"event": "api started."}})
    else:
        print("Graylog disabled. Not sending any Logs.")


def graylog_logger(level, handler, message):
    use_graylog = True
    if use_graylog:
        if handler == "mongodb":
            my_logger.info({"level": level, "handler": handler, "message": message})
        if level == "debug":
            my_logger.debug({"level": level, "handler": handler, "message": message})
        elif level == "warning":
            my_logger.warning({"level": level, "handler": handler, "message": message})
        elif level == "error":
            my_logger.error({"level": level, "handler": handler, "message": message})
        elif level == "info":
            my_logger.info({"level": level, "handler": handler, "message": message})
        else:
            print("ERROR: No valid log level specified.")
    else:
        print("Graylog disabled. Not sending any Logs.")
