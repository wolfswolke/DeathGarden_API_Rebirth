from flask_definitions import *
import os

from logic.mongodb_handler import mongo


@app.route("/gamenews/messages", methods=["GET"])
def gamenews():
    get_remote_ip()
    # /gamenews/messages?sortDesc=true&gameVersion=0&platform=PC&language=EN&messageType=InGameNews&faction=Runner&playerLevel=1
    try:
        sort_desc = request.args.get('sortDesc')
        gameVersion = request.args.get('gameVersion')
        platform = request.args.get('platform')
        language = request.args.get('language')
        messageType = request.args.get('messageType')
        faction = request.args.get('faction')
        playerLevel = request.args.get('playerLevel')
        output = json.load(open(os.path.join(app.root_path, "json", "placeholders", "gamenews.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-Game-News", message=e)


@app.route("/api/v1/config/VER_LATEST_CLIENT_DATA", methods=["GET"])
def config_ver_latest_client_data():
    get_remote_ip()
    try:
        return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-ver-latest-data", message=e)


@app.route("/api/v1/utils/contentVersion/latest/<version>", methods=["GET"])
def content_version_latest(version):
    get_remote_ip()
    try:
        print("Responded to content version api call GET")
        return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version", message=e)


@app.route("/gameservers.dev", methods=["POST", "GET"])
def gameservers_dev():
    get_remote_ip()
    try:
        # logger.graylog_logger(level="info", handler="logging_gameservers-dev", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=e)


@app.route("/gameservers.uat", methods=["POST"])
def gameservers_uat():
    get_remote_ip()
    try:
        # graylog_logger(request.get_json(), "warning")
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=e)
        return jsonify({"status": "error"})


@app.route("/gameservers.live", methods=["POST", "GET"])
def gameservers_live():
    get_remote_ip()
    try:
        # graylog_logger(request.get_json(), "warning")
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=e)


@app.route("/api/v1/config/UseMirrorsMM_Steam", methods=["GET"])  # What is this even???
def config_use_mirrors_mm_steam():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "value": "true"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-use-mirrors-mm-steam", message=e)


@app.route("/crashreport/unreal/CrashReporter/Ping", methods=["GET"])
def crashreporter_ping():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-crashreporter-ping", message=e)


@app.route("/tex", methods=["GET"])
def tex_get():
    get_remote_ip()
    try:
        return jsonify({"current-event": {}, "status": {}, "id": "live", "message": "Warning msg 1"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tex", message=e)


@app.route('/favicon.ico')
def favicon():
    get_remote_ip()
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    get_remote_ip()
    try:
        # return jsonify({"status": "success", "online": "true"})
        return jsonify({"Health": "Alive"})
        # {"Health": "Alive"}
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-healthcheck", message=e)


@app.route("/api/v1/services/tex")
def services_tex():
    get_remote_ip()
    try:
        return {"current-event": {"status": {"id": "live"}, "message": ""}}  # Alpha 2 WARNING Msg text?!?!
        # return jsonify({"status": "success", "online": "true", "Version": "te-18f25613-36778-ue4-374f864b",
        #                "ProjectID": "F72FA5E64FA43E878DC72896AD677FB5",
        #                "DefaultFactoryName": "HttpNetworkReplayStreaming", "ServeMatchDelayInMin": "30.0f"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-services-tex", message=e)


@app.route("/api/v1/consent/eula2", methods=["PUT", "GET"])
def consent_eula():
    get_remote_ip()
    try:
        if request.method == "PUT":
            userid = request.cookies.get('bhvrSession')
            try:
                mongo.eula(userId=userid, get_eula=False, server=mongo_host, db=mongo_db, collection=mongo_collection)
                return jsonify({"isGiven": True})
            except TimeoutError:
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="general-consent-eula",
                                      message=f"Error in consent_eula: {e}")
        elif request.method == "GET":
            if request.cookies.get('bhvrSession') is None:
                return jsonify({"isGiven": True})
            login_cookie = request.cookies.get('bhvrSession')
            is_given = mongo.get_data_with_list(login=login_cookie, login_steam=False,
                                                items={"eula"},
                                                server=mongo_host, db=mongo_db, collection=mongo_collection)
            if is_given:
                return jsonify({"isGiven": True})
            else:
                return jsonify({"isGiven": False})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula", message=e)


@app.route("/api/v1/consent/eula", methods=["GET"])
def consent_eula0():
    get_remote_ip()
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula0", message=e)


@app.route("/api/v1/consent/privacyPolicy", methods=["GET"])
def privacy_policy():
    get_remote_ip()
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-privacy-policy", message=e)


@app.route("/file/<game_version>/<seed>/<map_name>", methods=["POST", "GET"])
def file_gold_rush(seed, map_name, game_version):
    get_remote_ip()

    file_name = f"{game_version}_{seed}_{map_name}.raw"
    folder_path = os.path.join(app.root_path, "map_seeds")
    file_path = os.path.join(folder_path, file_name)
    os.makedirs(folder_path, exist_ok=True)

    if request.method == "GET":
        if os.path.isfile(file_path):
            with open(file_path, "rb") as files:
                data = files.read()
                return data

    if request.method == "POST":
        data = request.get_data()
        with open(file_path, "wb") as files:
            files.write(data)
        return {"status": "success"}


@app.route("/api/v1/extensions/leaderboard/getScores", methods=["GET", "POST"])
def leaderboard_get_scores():
    get_remote_ip()
    if request.method == "POST":
        logger.graylog_logger(level="info", handler="general-leaderboard-get-scores",
                              message=f"Leaderboard getScores: {request.get_json()}")
        data = json.load(open(os.path.join(app.root_path, "json", "placeholders", "leaderboard.json"), "r"))
        return jsonify(data)
    else:
        try:
            return jsonify({"data": []})
        except TimeoutError:
            return jsonify({"status": "error"})
        except Exception as e:
            logger.graylog_logger(level="error", handler="general-leaderboard-get-scores", message=e)


@app.route("/submit/", methods=["POST"])
def submit():
    get_remote_ip()
    return "Discarded=1"


@app.route("/api/v1/extensions/quitters/getQuitterState", methods=["POST"])
def get_quitter_state():
    get_remote_ip()
    try:
        logger.graylog_logger(level="info", handler="logging_getQuitterState", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getQuitterState", message=e)
