from flask_definitions import *
import time
import uuid
import bleach


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
        if user_agent.startswith("TheExit/++UE4+Release-4.2"):
            _get_remote_ip("strict")
        elif user_agent.startswith("game=TheExit, engine=UE4, version="):
            _get_remote_ip("strict")
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

    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        expires = time.time() + 3600
        self.sessions[session_id] = {"session_id": session_id, "expires": expires, "user": user_id}
        return session_id

    def get_user_id(self, session_id):
        self.clean_sessions()
        if session_id not in self.sessions:
            logger.graylog_logger(level="info", handler="session_manager", message=f"Session ID: {session_id} not found.")
            return None
        self.extend_session(session_id)
        return self.sessions[session_id]["user"]

    def extend_session(self, session_id):
        session_expires = self.sessions[session_id]["expires"]
        if session_expires <= 3600:
            self.sessions[session_id]["expires"] = time.time() + 4600
        else:
            pass

    def clean_sessions(self):
        current_time = time.time()
        if self.sessions == {}:
            return
        expired_sessions = [session_id for session_id, data in self.sessions.items() if data["expires"] < current_time]
        for session_id in expired_sessions:
            self.sessions.pop(session_id)


session_manager = Session_Manager()
