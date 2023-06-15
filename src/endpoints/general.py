import base64

import flask_definitions
from flask_definitions import *
import os


@app.route("/gamenews/messages", methods=["GET"])
def gamenews():
    get_remote_ip()
    try:
        print("Responded to game news api call GET")
        return jsonify({"news": [
            {"contentTags": ["steam", "xbox", "ps4", "grdk", "xsx", "ps5", "egs", "stadia", "switch"],
             "description": "It's not The Clown's Bottles making you see double.<br/><br/>From September 1st 11AM ET - September 8th 11AM ET, earn twice the XP from Trials and Emblems.",
             "dwnImagePath": "", "imageHeight": "", "imagePath": "", "isHidden": False,
             "startDate": "2022-09-01T15:00:00", "title": "Double XP Event", "type": 5, "version": "6.2.0",
             "weight": 40990.0}]})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-Game-News", message=f"Error in gamenews: {e}")


@app.route("/api/v1/config/VER_LATEST_CLIENT_DATA", methods=["GET"])
def config_ver_latest_client_data():
    get_remote_ip()
    try:
        print("Responded to config ver latest client data api call GET")
        return jsonify({"status": "success", "value": "6.2.0"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-ver-latest-data", message=f"Error in config_ver_latest_client_data: {e}")


@app.route("/api/v1/utils/contentVersion/latest/2.2", methods=["GET"])
def content_version_latest():
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({"availableVersions": {
            "10.0.19045.1.256live": "te-18f25613-36778-ue4-374f864b",
            "3.3.0_241792live": "te-f9b4768a-26590-ue4-cefc1aee",
            "3.3.0_244688live": "3.3.0_244688live-1573508813"}})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version", message=f"Error in content_version_latest: {e}")


@app.route("/gameservers.dev", methods=["POST"])
def gameservers_dev():
    get_remote_ip()
    try:
        print("Responded to Gameserver event api call POST")
        # graylog_logger(request.get_json(), "warning")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=f"Error in gameservers_dev: {e}")


@app.route("/api/v1/config/UseMirrorsMM_Steam", methods=["GET"])
def config_use_mirrors_mm_steam():
    get_remote_ip()
    try:
        print("Responded to config use mirrors mm steam api call GET")
        return jsonify({"status": "success", "value": "true"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-use-mirrors-mm-steam", message=f"Error in config_use_mirrors_mm_steam: {e}")


@app.route("/crashreport/unreal/CrashReporter/Ping", methods=["GET"])
def crashreporter_ping():
    get_remote_ip()
    try:
        print("Responded to crashreporter ping api call GET")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-crashreporter-ping", message=f"Error in crashreporter_ping: {e}")


@app.route("/tex", methods=["GET"])
def tex_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tex", message=f"Error in tex_get: {e}")


@app.route("/")
def root():
    try:
        get_remote_ip()
        return jsonify({"status": "success"})
        # return render_template("index.html")
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-root", message=f"Error in root: {e}")


@app.route('/favicon.ico')
def favicon():
    get_remote_ip()
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=f"Error in favicon: {e}")


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "online": "true"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-healthcheck", message=f"Error in healthcheck: {e}")


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
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-services-tex", message=f"Error in services_tex: {e}")


@app.route("/api/v1/utils/contentVersion/latest/2.11", methods=["GET"])
def content_version():
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({
                           "latestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})  # Don't know if this is correct. Just testing.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version", message=f"Error in content_version: {e}")


@app.route("/api/v1/utils/contentVersion/latest/0", methods=["GET"])
def content_version0():
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({
            "latestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})  # Don't know if this is correct. Just testing.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version0", message=f"Error in content_version0: {e}")


@app.route("/api/v1/utils/contentVersion/latest/1.1", methods=["GET"])
def content_version1():
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({
            "latestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})  # Don't know if this is correct. Just testing.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version1", message=f"Error in content_version1: {e}")


@app.route("/api/v1/consent/eula2", methods=["PUT", "GET"])
def consent_eula():
    get_remote_ip()
    if request.method == "PUT":
        try:
            print("Responded to consent eula api call PUT")
            return jsonify({"status": "success"})
        except TimeoutError:
            print("Timeout error")
            return jsonify({"status": "error"})
        except Exception as e:
            logger.graylog_logger(level="error", handler="general-consent-eula", message=f"Error in consent_eula: {e}")
    elif request.method == "GET":
        try:
            print("Responded to consent eula api call GET")
            return jsonify({"isGiven": True})
        except TimeoutError:
            print("Timeout error")
            return jsonify({"status": "error"})
        except Exception as e:
            logger.graylog_logger(level="error", handler="general-consent-eula", message=f"Error in consent_eula: {e}")


@app.route("/api/v1/consent/eula", methods=["GET"])
def consent_eula0():
    get_remote_ip()
    try:
        print("Responded to consent eula api call GET")
        return jsonify({"id": "eula", "language": ["de", "en", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pl",
                                                   "pt-BR", "ru", "sv", "th", "tr", "zh-Hans", "zh-Hant"],
                        "platform": ["steam", "xbox", "xsx", "switch", "grdk", "stadia"]})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula0", message=f"Error in consent_eula0: {e}")


@app.route("/api/v1/consent/privacyPolicy", methods=["GET"])
def privacy_policy():
    get_remote_ip()
    try:
        print("Responded to consent privacyPolicy api call GET")
        return jsonify({"id":"privacy","language":["de","en","es","es-MX","fr","it","ja","ko","nl","pl","pt-BR","ru",
                                                   "sv","th","tr","zh-Hans","zh-Hant"],
                        "platform":["steam","xbox","xsx","switch","grdk","ps4","ps5","stadia"]})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-privacy-policy", message=f"Error in consent_eula0: {e}")


@app.route("/api/v1/utils/contentVersion/latest/2.5", methods=["GET"])
def content_version2_5():
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({
            "latestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})  # Don't know if this is correct. Just testing.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version2_5", message=f"Error in content_version2_5: {e}")


@app.route("/file/<game_version>/<seed>/<map_name>", methods=["POST", "GET"])
def file_gold_rush(seed, map_name, game_version):
    get_remote_ip()

    print(game_version)
    print(seed)
    print(map_name)

    file_name = f"{game_version}_{seed}_{map_name}.b64"
    folder_path = os.path.join(app.root_path, "map_seeds")
    file_path = os.path.join(folder_path, file_name)
    os.makedirs(folder_path, exist_ok=True)

    if request.method == "GET":
        if os.path.isfile(file_path):
            with open(file_name, "r") as files:
                data = files.read()
                encoded_data = base64.b64encode(data)
                return encoded_data

    if request.method == "POST":
        data = request.get_data()
        decoded_data = base64.b64decode(data)
        with open(file_path, "wb") as files:
            files.write(decoded_data)
        return {"status": "success"}

