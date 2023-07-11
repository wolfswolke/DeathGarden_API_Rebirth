import logging
import graypy
import json


class Logger:
    def __init__(self):
        self.my_logger = logging.getLogger('deathgarden_api')
        self.dynamic_use_graylog = False

    def setup_graylog(self, use_graylog, graylog_server):
        self.dynamic_use_graylog = use_graylog
        if self.dynamic_use_graylog:
            self.my_logger.setLevel(logging.DEBUG)
            handler = graypy.GELFUDPHandler(graylog_server, 12201)
            self.my_logger.addHandler(handler)
            self.graylog_logger(level="info", handler="logging_server_Event", message={"event": "api started"})
        else:
            print("Graylog disabled. Not sending any Logs.")

    def graylog_logger(self, level, handler, message):
        use_graylog = True
        if use_graylog:
            log_methods = {"debug": self.my_logger.debug, "warning": self.my_logger.warning,
                           "error": self.my_logger.error, "info": self.my_logger.info}
            log_method = log_methods.get(level)
            if log_method:
                message = json.dumps({"level": level, "handler": handler, "message": message})
                log_method(message)
            else:
                print("ERROR: No valid log level specified.")
        else:
            print("Graylog disabled. Not sending any Logs.")


logger = Logger()
