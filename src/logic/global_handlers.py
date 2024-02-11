from flask_definitions import *
import time
import uuid
import bleach
import os
import json


def _get_remote_ip(check_type="strict"):
    if check_type == "strict":
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_addr = request.environ['REMOTE_ADDR']
            if ip_addr == "127.0.0.1":
                return None
            logger.graylog_logger(level="info", handler="ip_handler", message=f"New Connection from: {ip_addr}")
            return ip_addr
        else:
            ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
            if ip_addr == "127.0.0.1":
                return None
            else:
                logger.graylog_logger(level="info", handler="ip_handler", message=f"New Connection from: {ip_addr}")
                return ip_addr
    else:
        return "127.0.0.1"


def check_for_game_client(check_type="strict"):
    if check_type == "strict":
        user_agent = sanitize_input(request.headers.get('User-Agent'))
        if user_agent.startswith("TheExit/++UE4+Release-4.21-CL-0"):
            _get_remote_ip("strict")
        # elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        #    _get_remote_ip("strict")
        elif user_agent.startswith("CrashReportClient/++UE4+Release-4.21"):
            _get_remote_ip("strict")
        elif user_agent.startswith("CrashReportClient/++UE4+Release-4.20-CL-0"):
            _get_remote_ip("strict")
        elif user_agent.startswith("CrashReportClient, engine=UE4"):
            _get_remote_ip("strict")
        else:
            _get_remote_ip()
            logger.graylog_logger(level="info", handler="UserAgents", message=f"INVALID User-Agent: {user_agent} "
                                                                              f"from IP: {_get_remote_ip()}")
            print(f"INVALID User-Agent: {user_agent}, IP: {_get_remote_ip()}")
            abort(403)
    elif check_type == "remote":
        remote = _get_remote_ip()
        return remote
    else:
        _get_remote_ip("soft")


def sanitize_input(input_value):
    if input_value is None:
        return None
    return bleach.clean(input_value)


class Session_Manager:
    def __init__(self):
        self.sessions = {}
        self.session_file = "sessions.json"
        # Relative Path /app/tmp/sessions.json
        self.session_file_path = f"/app/tmp/{self.session_file}"

    def setup(self):
        print("Setting up Session Manager")
        print(f"Session File Path: {self.session_file_path}")
        if not os.path.exists(self.session_file_path):
            print("Session File not found, creating new one.")
            with open(self.session_file_path, "w") as session_file:
                session_file.write("{}")
        with open(self.session_file_path, "r") as session_file:
            print("Loading Sessions")
            self.sessions = json.load(session_file)
            print(f"DEBUG Sessions: {self.sessions}")

    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        expires = time.time() + 3600
        self.sessions[session_id] = {"session_id": session_id, "expires": expires, "user": user_id}
        self.save_sessions(clean=True)
        return session_id

    def get_user_id(self, session_id):
        self.clean_sessions()
        if session_id not in self.sessions:
            if session_id:
                return None
            else:
                logger.graylog_logger(level="info", handler="session_manager",
                                  message=f"Session ID: {session_id} not found.")
                return None
        self.extend_session(session_id)
        self.save_sessions()
        return self.sessions[session_id]["user"]

    def extend_session(self, session_id):
        self.sessions[session_id]["expires"] = time.time() + 3600
        self.save_sessions()

    def clean_sessions(self):
        current_time = time.time()
        if self.sessions == {}:
            return
        for session in self.sessions:
            if self.sessions[session]["expires"] < current_time:
                self.sessions.pop(session)

    def __write_sessions__(self):
        with open(self.session_file_path, "w") as session_file:
            json.dump(self.sessions, session_file)

    def save_sessions(self, clean=False):
        if clean:
            self.clean_sessions()
        self.__write_sessions__()


session_manager = Session_Manager()
