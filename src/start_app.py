"""

"""
# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from flask import Flask, send_from_directory, request, jsonify
from threading import Thread
import os
import yaml

from logic.Elasticsearch_handler import es_upload


# ------------------------------------------------------- #
# functions
# ------------------------------------------------------- #
def load_config():
    with open('config//api_config.yaml', 'r') as f:
        config_file = yaml.safe_load(f)
    return config_file


app = Flask(__name__)


@app.route("/")
def root():
    return "<p>Development Server for Death Garden API!</p>"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    print("Responded to Metrics api call POST")
    data = request.get_json()
    es_upload(server=es_server, index="client_event", log_message=data)
    return jsonify({"status": "success"})


@app.route("/metrics/httplog/event", methods=["POST"])
def metrics_httplog_event():
    data = request.get_json()
    es_upload(server=es_server, index="metrics_httplog_event", log_message=data)
    return jsonify({"status": "success"})


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "success", "online": "true"})


@app.route("/api/v1/services/tex")
def services_tex():
    print("Responded to tex api call GET")
    return jsonify({"status": "success", "online": "true", "Version": "te-18f25613-36778-ue4-374f864b",
                    "ProjectID": "F72FA5E64FA43E878DC72896AD677FB5",
                    "DefaultFactoryName": "HttpNetworkReplayStreaming", "ServeMatchDelayInMin": "30.0f"})


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    print("Responded to analytics api call POST")
    data = request.get_json()
    es_upload(server=es_server, index="game_data_analytics", log_message=data)
    return jsonify({"status": "success"})


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    print("Responded to analytics batch api call POST")
    data = request.get_json()
    es_upload(server=es_server, index="game_data_analytics_batch", log_message=data)
    return jsonify({"status": "success"})


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    steam_token = request.args.get('token')
    es_upload(server=es_server, index="steam_login", log_message=steam_token)
    # return jsonify({"clientData":{"catalogId": "3.6.0_281460live", "consentId": "3.6.0_281460live"}})
    return jsonify({"clientData": "3.0.1"})


# [Backend]
@app.route("/tex", methods=["GET"])
def tex_get():
    return jsonify({"status": "success"})


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)

    t.start()


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #

config = load_config()
es_server = config['elasticsearch']['host']


# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
keep_alive()
print("Exiting...")
exit(0)
