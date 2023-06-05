"""

"""
import logging

# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from flask import Flask, send_from_directory, request, jsonify, render_template, make_response
from threading import Thread
import os
import yaml
import graypy


# ------------------------------------------------------- #
# functions
# ------------------------------------------------------- #
def load_config():
    with open('config//api_config.yaml', 'r') as f:
        config_file = yaml.safe_load(f)
    return config_file


def setup_graylog():
    if use_graylog:
        global my_logger
        my_logger = logging.getLogger('deathgarden_api')
        my_logger.setLevel(logging.DEBUG)
        handler = graypy.GELFUDPHandler(graylog_server, 12201)
        my_logger.addHandler(handler)
        my_logger.debug('Started Death Garden API')
    else:
        print("Graylog disabled. Not sending any Logs.")


def graylog_logger(message, level):
    if use_graylog:
        if level == "debug":
            my_logger.debug(message)
        if level == "warning":
            my_logger.warning(message)
        if level == "error":
            my_logger.error(message)
        if level == "info":
            my_logger.info(message)
    else:
        print("Graylog disabled. Not sending any Logs.")


def get_remote_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_addr = request.environ['REMOTE_ADDR']
    else:
        ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
    print("New Connection from: " + ip_addr)


app = Flask(__name__)


@app.route("/")
def root():
    get_remote_ip()
    return jsonify({"status": "success"})
    # return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    get_remote_ip()
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    get_remote_ip()
    try:
        print("Responded to Metrics api call POST")
        data = request.get_json()
        graylog_logger("Metric API: " + str(data), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/metrics/httplog/event", methods=["POST"])
def metrics_httplog_event():
    get_remote_ip()
    try:
        data = request.get_json()
        graylog_logger("Upload: " + str(data), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "online": "true"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/api/v1/services/tex")
def services_tex():
    get_remote_ip()
    try:
        print("Responded to tex api call GET")
        return {"status": "success"}
        # return jsonify({"status": "success", "online": "true", "Version": "te-18f25613-36778-ue4-374f864b",
        #                "ProjectID": "F72FA5E64FA43E878DC72896AD677FB5",
        #                "DefaultFactoryName": "HttpNetworkReplayStreaming", "ServeMatchDelayInMin": "30.0f"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    get_remote_ip()
    try:
        print("Responded to analytics api call POST")
        data = request.get_json()
        graylog_logger("DataAnalytics: " + str(data), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    get_remote_ip()
    try:
        print("Responded to analytics batch api call POST")
        data = request.get_json()
        graylog_logger("Batch upload: " + str(data), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    get_remote_ip()
    # Here the Client sends a signed session ticket as a hex string to the Server.
    # In return, it wants a cookie named bhvrSession.
    # The Session Ticket allways starts with: 14000000
    try:
        steam_session_token = request.args.get('token')
        graylog_logger("Login by Session Ticket: " + steam_session_token, "info")
        response = make_response()
        # This is a TEST cookie. It does NOT work!
        response.set_cookie("bhvrSession", '0ShiciK0Gthwlc_wrvDAE6A.x0Ye670Dwfe3X657Z2Y2tfkIEoM0a13Mqzm-FErDacC2pKpUJPeyAjEApxgJGFIiS4__blAn4zsk0FOHL-PtUOxHSTWCEc_FKMb2RL41KJBKAXdnGcvCw-4PRLuSfxMBrN9FErAwwbRV9HIKSH39vpm-mpAwmVVCNiQK3XD2T1Ud2N0fiJPHHqvHNiXfOoclQZL3qcnu-fMa6NS4qxEpkS1RwtjSJ1FI9eWFZtlZodvpTiTHnPnadcz22G8lhAi9a.1603079556863.86400000.4U3 4PGSyJ8YEVvATGkmJhiCeCIPuHaD7MVXzPaGYYZ8')
        return response
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


# [Backend]
@app.route("/tex", methods=["GET"])
def tex_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)

    t.start()


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']


# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
setup_graylog()
keep_alive()
print("Exiting...")
exit(0)
