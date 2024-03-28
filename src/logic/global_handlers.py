import ipaddress

from flask_definitions import *
import time
import uuid
import bleach
import os
import json


def check_bogon_ip(ip_addr):
    bogon_ranges = [
        "0.0.0.0/8",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "127.0.0.0/8",
        "127.0.53.53",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.0.0.0/24",
        "192.0.2.0/24",
        "192.168.0.0/16",
        "198.18.0.0/15",
        "198.51.100.0/24",
        "203.0.113.0/24",
        "224.0.0.0/4",
        "240.0.0.0/4",
        "255.255.255.255/32",
        "::/128",
        "::1/128",
        "::ffff:0:0/96",
        "::/96",
        "100::/64",
        "2001:10::/28",
        "2001:db8::/32",
        "fc00::/7",
        "fe80::/10",
        "fec0::/10",
        "ff00::/8",
        "2002::/24",
        "2002:a00::/24",
        "2002:7f00::/24",
        "2002:a9fe::/32",
        "2002:ac10::/28",
        "2002:c000::/40",
        "2002:c000:200::/40",
        "2002:c0a8::/32",
        "2002:c612::/31",
        "2002:c633:6400::/40",
        "2002:cb00:7100::/40",
        "2002:e000::/20",
        "2002:f000::/20",
        "2002:ffff:ffff::/48",
        "2001::/40",
        "2001:0:a00::/40",
        "2001:0:7f00::/40",
        "2001:0:a9fe::/48",
        "2001:0:ac10::/44",
        "2001:0:c000::/56",
        "2001:0:c000:200::/56",
        "2001:0:c0a8::/48",
        "2001:0:c612::/47",
        "2001:0:c633:6400::/56",
        "2001:0:cb00:7100::/56",
        "2001:0:e000::/36",
        "2001:0:f000::/36",
        "2001:0:ffff:ffff::/64"
    ]
    for bogon_range in bogon_ranges:
        ip_addr_obj = ipaddress.ip_address(ip_addr)
        network = ipaddress.ip_network(bogon_range)
        if ip_addr_obj in network:
            return True
    return False


def _get_remote_ip(check_type="strict"):
    if check_type == "strict":
        if request.environ.get('HTTP_CF_CONNECTING_IP'):
            ip_addr = request.environ['HTTP_CF_CONNECTING_IP']
            if ip_addr == "192.168.1.111" or ip_addr == "192.168.1.130":
                return None
            logger.graylog_logger(level="info", handler="ip_handler", message=f"New Connection from: {ip_addr}")
            bogon_check = check_bogon_ip(ip_addr)
            if bogon_check:
                logger.graylog_logger(level="info", handler="ip_handler", message=f"BOGON IP DETECTED: {ip_addr}")
                abort(403)
            return ip_addr
        elif request.environ.get('HTTP_X_FORWARDED_FOR'):
            ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
            if ip_addr == "127.0.0.1":
                return None
            else:
                bogon_check = check_bogon_ip(ip_addr)
                if bogon_check:
                    logger.graylog_logger(level="info", handler="ip_handler", message=f"BOGON IP DETECTED: {ip_addr}")
                    abort(403)
                logger.graylog_logger(level="info", handler="ip_handler", message=f"New Connection from: {ip_addr}")
                return ip_addr
        else:
            ip_addr = request.remote_addr
            if ip_addr == "127.0.0.1":
                return None
            else:
                bogon_check = check_bogon_ip(ip_addr)
                if bogon_check:
                    logger.graylog_logger(level="info", handler="ip_handler", message=f"BOGON IP DETECTED: {ip_addr}")
                    abort(403)
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
        elif user_agent.startswith("TheExit/++UE4+Release-4.20-CL-0"):
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
                logger.graylog_logger(level="info", handler="session_manager",
                                  message=f"Session ID: {session_id} not found.")
                abort(401)
            else:
                abort(401)
        self.extend_session(session_id)
        self.save_sessions()
        return self.sessions[session_id]["user"]

    def extend_session(self, session_id):
        try:
            self.sessions[session_id]["expires"] = time.time() + 3600
            self.save_sessions()
        except KeyError:
            logger.graylog_logger(level="info", handler="session_manager",
                                  message=f"Session ID: {session_id} not found.")
            abort(403)

    def clean_sessions(self):
        current_time = time.time()
        if self.sessions == {}:
            return
        temp_sessions = dict(self.sessions)
        for session in temp_sessions:
            if temp_sessions[session]["expires"] < current_time:
                self.sessions.pop(session)

    def __write_sessions__(self):
        with open(self.session_file_path, "w") as session_file:
            json.dump(self.sessions, session_file)

    def save_sessions(self, clean=False):
        if clean:
            self.clean_sessions()
        self.__write_sessions__()


session_manager = Session_Manager()
