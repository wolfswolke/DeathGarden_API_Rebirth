import logging
import sys
import graypy
import json
import traceback
import os
from colorlog import ColoredFormatter


class Logger:
    def __init__(self):
        self.my_logger = logging.getLogger('deathgarden_api')
        self.dynamic_use_graylog = False

    def setup_graylog(self, use_graylog, graylog_server):
        self.dynamic_use_graylog = use_graylog
        if os.environ['DEV'] == "true":
            self.my_logger.setLevel(logging.DEBUG)
        else:
            self.my_logger.setLevel(logging.INFO)
        if self.dynamic_use_graylog:
            handler = graypy.GELFUDPHandler(graylog_server, 12201)
            self.my_logger.addHandler(handler)
        else:
            print("Graylog disabled. Not sending any Logs.")
        self.graylog_logger(level="info", handler="logging_server_Event", message={"event": "api started"})

    def graylog_logger(self, level, handler, message):
        use_graylog = True
        if use_graylog:
            formatter = ColoredFormatter(
                "%(log_color)s%(asctime)s %(levelname)-8s%(reset)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                reset=True,
                log_colors={
                    'DEBUG': 'blue',
                    'INFO': 'white',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'red,bg_white',
                }
            )
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            self.my_logger.addHandler(console_handler)
            log_methods = {"debug": self.my_logger.debug, "warning": self.my_logger.warning,
                           "error": self.my_logger.error, "info": self.my_logger.info,
                           "critical": self.my_logger.critical}
            log_method = log_methods.get(level)
            if log_method:
                try:
                    message = json.dumps({"level": level, "handler": handler, "message": message})
                except TypeError:
                    message = f"{{\"level\": \"{level}\", \"handler\": \"{handler}\", \"message\": \"{str(message)}\"}}"
                if level == "error":
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    tb_str = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    message = f"{message}\n{''.join(tb_str)}"

                log_method(message)
            else:
                print("ERROR: No valid log level specified.")
            self.my_logger.removeHandler(console_handler)
        else:
            print("Graylog disabled. Not sending any Logs.")


logger = Logger()
