from flask_definitions import *
import os

from logic.mongodb_handler import mongo


@app.route("/gamenews/messages", methods=["GET"])
def gamenews():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
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
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-ver-latest-data", message=e)


@app.route("/api/v1/utils/contentVersion/latest/<version>", methods=["GET"])
def content_version_latest(version):
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        print("Responded to content version api call GET")
        return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-content-version", message=e)


@app.route("/gameservers.dev", methods=["POST", "GET"])
def gameservers_dev():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        # logger.graylog_logger(level="info", handler="logging_gameservers-dev", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=e)


@app.route("/gameservers.uat", methods=["POST"])
def gameservers_uat():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
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
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        # graylog_logger(request.get_json(), "warning")
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=e)


@app.route("/api/v1/config/UseMirrorsMM_Steam", methods=["GET"])  # What is this even???
def config_use_mirrors_mm_steam():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify("false")
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-use-mirrors-mm-steam", message=e)


@app.route("/crashreport/unreal/CrashReporter/Ping", methods=["GET"])
def crashreporter_ping():
    check_for_game_client("soft")
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-crashreporter-ping", message=e)


@app.route("/tex", methods=["GET"])
def tex_get():
    check_for_game_client("soft")
    try:
        return jsonify({"current-event": {}, "status": {}, "id": "live", "message": "Warning msg 1"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tex", message=e)


@app.route('/favicon.ico')
def favicon():
    check_for_game_client("soft")
    try:
        return send_from_directory(os.path.join(app.root_path, 'image'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-favicon", message=e)


@app.route("/api/v1/healthcheck", methods=["GET"])
def healthcheck():
    check_for_game_client("soft")
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
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        if request.method == "PUT":

            session_cookie = request.cookies.get("bhvrSession")
            if not session_cookie:
                return jsonify({"message": "Endpoint not found"}), 404
            userid = session_manager.get_user_id(session_cookie)
            if userid == 401:
                return jsonify({"message": "Endpoint not found"}), 404

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
            session_cookie = request.cookies.get("bhvrSession")
            if not session_cookie:
                return jsonify({"message": "Endpoint not found"}), 404
            userid = session_manager.get_user_id(session_cookie)
            if userid == 401:
                return jsonify({"message": "Endpoint not found"}), 404
            is_given = mongo.get_data_with_list(login=userid, login_steam=False,
                                                items={"eula"},
                                                server=mongo_host, db=mongo_db, collection=mongo_collection)
            if is_given["eula"]:
                return jsonify({"isGiven": True})
            else:
                return jsonify({"isGiven": False})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula", message=e)


@app.route("/api/v1/consent/eula", methods=["GET"])
def consent_eula0():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-consent-eula0", message=e)


@app.route("/api/v1/consent/privacyPolicy", methods=["GET"])
def privacy_policy():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    session_cookie = request.cookies.get("bhvrSession")
    if not session_cookie:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = session_manager.get_user_id(session_cookie)
    if userid == 401:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        output = json.load(open(os.path.join(app.root_path, "json", "eula.json"), "r"))
        return jsonify(output)
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-privacy-policy", message=e)


@app.route("/api/v1/extensions/leaderboard/getScores", methods=["GET", "POST"])
def leaderboard_get_scores():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    session_cookie = request.cookies.get("bhvrSession")
    if not session_cookie:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = session_manager.get_user_id(session_cookie)
    if userid == 401:
        return jsonify({"message": "Endpoint not found"}), 404
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
    check = check_for_game_client("soft")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    return "Discarded=1"


@app.route("/api/v1/extensions/quitters/getQuitterState", methods=["POST"])
def get_quitter_state():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    session_cookie = request.cookies.get("bhvrSession")
    if not session_cookie:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = session_manager.get_user_id(session_cookie)
    if userid == 401:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="logging_getQuitterState", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getQuitterState", message=e)
