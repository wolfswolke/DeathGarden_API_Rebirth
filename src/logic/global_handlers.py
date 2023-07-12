from flask_definitions import *
import yaml


def _get_remote_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_addr = request.environ['REMOTE_ADDR']
        print("New Connection from: " + ip_addr)
        return ip_addr
    else:
        ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
        if ip_addr == "127.0.0.1":
            return None
        else:
            print("New Connection from: " + ip_addr)
            return ip_addr


def load_config():
    with open('config//api_config.yaml', 'r') as f:
        config_file = yaml.safe_load(f)
    return config_file


def check_for_game_client(check_type="strict"):
    if check_type == "strict":
        user_agent = request.headers.get('User-Agent')
        if user_agent.startswith("TheExit/++UE4+Release-4.2"):
            _get_remote_ip()
            # logger.graylog_logger(level="info", handler="UserAgents", message=f"User-Agent: {user_agent}")
            return True
        elif user_agent.startswith("game=TheExit, engine=UE4, version="):
            _get_remote_ip()
            # logger.graylog_logger(level="info", handler="UserAgents", message=f"User-Agent: {user_agent}")
            return True

        else:
            _get_remote_ip()
            # logger.graylog_logger(level="error", handler="UserAgents", message=f"INVALID User-Agent: {user_agent}, "
            #                                                                   f"with IP: {_get_remote_ip()}")
            return False
    else:
        _get_remote_ip()
        return True

