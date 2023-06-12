from flask_definitions import *
import os


@app.route("/file/te-f9b4768a-26590-ue4-cefc1aee/1686509333/Survival-Biome_Definition_DES_Mayan", methods=["POST"])
def file_survival_biome_definition_des_mayan():
    get_remote_ip()
    try:
        print("Responded to file survival biome definition des mayan api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/gamenews/messages", methods=["GET"])
def gamenews():
    get_remote_ip()
    try:
        print("Responded to aaaaa api call GET")
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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/tex", methods=["GET"])
def tex_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/")
def root():
    try:
        get_remote_ip()
        return jsonify({"status": "success"})
        # return render_template("index.html")
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "online": "true"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


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
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/consent/eula2", methods=["GET"])
def consent_eula():
    get_remote_ip()
    try:
        print("Responded to consent eula api call GET")
        return jsonify({"status": "success", "consent": "true"})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"id": "eula", "language": ["de", "en", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pl",
                                                   "pt-BR", "ru", "sv", "th", "tr", "zh-Hans", "zh-Hant"],
                        "platform": ["steam", "xbox", "xsx", "switch", "grdk", "stadia"]})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/consent/eula", methods=["GET"])
def consent_eula0():
    get_remote_ip()
    try:
        print("Responded to consent eula api call GET")
        return jsonify({"status": "success", "consent": "true"})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"id": "eula", "language": ["de", "en", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pl",
                                                   "pt-BR", "ru", "sv", "th", "tr", "zh-Hans", "zh-Hant"],
                        "platform": ["steam", "xbox", "xsx", "switch", "grdk", "stadia"]})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")
