import datetime

from flask_definitions import *
import yaml
import time
import uuid


def _get_remote_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_addr = request.environ['REMOTE_ADDR']
        if ip_addr == "127.0.0.1":
            return None
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


class Session_Manager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        expires = time.time() + 3600
        self.sessions[session_id] = {"session_id": session_id, "expires": expires, "user": user_id}
        return session_id

    def get_user_id(self, session_id):
        self.clean_sessions()
        if session_id not in self.sessions:
            return 401
        self.extend_session(session_id)
        return self.sessions[session_id]["user"]

    def extend_session(self, session_id):
        self.sessions[session_id]["expires"] = time.time() + 3600

    def clean_sessions(self):
        current_time = time.time()
        if self.sessions == {}:
            return
        expired_sessions = [session_id for session_id, data in self.sessions.items() if data["expires"] < current_time]
        for session_id in expired_sessions:
            self.sessions.pop(session_id)


session_manager = Session_Manager()
