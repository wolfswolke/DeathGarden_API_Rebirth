from flask import Flask, send_from_directory, request, jsonify
from threading import Thread
from logic.handler import post_handler
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def hello_world():
    return "<p>Development Server for Death Garden API!</p>"


@app.route("/api/v1/services/tex")
def one():
    print("Responded to tex api call GET")
    return jsonify({"status": "success", "online": "true", "Version": "te-18f25613-36778-ue4-374f864b",
                    "ProjectID": "F72FA5E64FA43E878DC72896AD677FB5",
                    "DefaultFactoryName": "HttpNetworkReplayStreaming", "ServeMatchDelayInMin": "30.0f"})


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    print("Responded to Metrics api call POST")
    data = request.get_json()
    post_handler(data)
    return jsonify({"status": "success"})


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "success", "online": "true"})


@app.route("/metrics/httplog/event", methods=["POST"])
def receive_event2():
    print("Responded to httplog api call POST")
    data = request.get_json()
    post_handler(data)
    return jsonify({"status": "success"})


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    print("Responded to analytics api call POST")
    data = request.get_json()
    post_handler(data)
    return jsonify({"status": "success"})


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    print("Responded to analytics batch api call POST")
    data = request.get_json()
    post_handler(data)
    return jsonify({"status": "success"})


# [Backend]
@app.route("/tex", methods=["GET"])
def tex_get():
    return jsonify({"status": "success"})


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # here we want to get the value of user (i.e. ?user=some-value)
    steam_token = request.args.get('token')
    print(steam_token)
    # return jsonify({"clientData":{"catalogId": "3.6.0_281460live", "consentId": "3.6.0_281460live"}})
    return jsonify({"clientData": "3.0.1"})


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)

    t.start()


try:
    keep_alive()
except KeyboardInterrupt:
    print("Exiting...")
    exit(0)
