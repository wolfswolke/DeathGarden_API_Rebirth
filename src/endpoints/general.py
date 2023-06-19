import base64

import flask_definitions
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
        print("Responded to game news api call GET")
        return {"data": [
  {
    "Id": "1",
    "MessageType": 2,
    "IsOneTimeGameNews": False,
    "ShouldQuitTheGame": False,
    "OnlyForPlayersThatCompletedAtLeastOneMatch": False,
    "RedirectMode": 0,
    "RedirectItem": "",
    "RedirectUrl": "",
    "EmbeddedBackgroundImage": "game/UI/ImageAssets/NewsAssets/GeneralAnnouncement_Large",
    "EmbeddedInGameNewsBackgroundImage": "game/UI/ImageAssets/NewsAssets/ClosedAlphaWelcomseBanner",
    "EmbeddedInGameNewsThumbnailImage": "game/UI/ImageAssets/NewsAssets/CrossPromo",
    "FromDate": 1655511433,
    "ToDate": 1718669833,
    "Translations": [
      {
        "Language": 0,
        "Body": "Test EN"
      },
      {
        "Language": 1,
        "Body": "Test Fr"
      },
      {
        "Language": 2,
        "Body": "Test IT"
      },
      {
        "Language": 3,
        "Body": "Test Es"
      }
    ]
  }
]}
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


@app.route("/api/v1/utils/contentVersion/latest/<version>", methods=["GET"])
def content_version_latest(version):
    print("Versions = " + version)
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


@app.route("/gameservers.dev", methods=["POST", "GET"])
def gameservers_dev():
    get_remote_ip()
    try:
        print("Responded to Gameserver event api call POST")
        # logger.graylog_logger(level="info", handler="logging_gameservers-dev", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-gameserver-dev", message=f"Error in gameservers_dev: {e}")


@app.route("/gameservers.uat", methods=["POST"])
def gameservers_uat():
    get_remote_ip()
    try:
        print("Responded to Gameserver event api call POST")
        # graylog_logger(request.get_json(), "warning")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        # logger.graylog_logger(level="error", handler="general-gameserver-dev", message=f"Error in gameservers_dev: {e}")
        print(e)
        return jsonify({"status": "error"})


@app.route("/gameservers.live", methods=["POST", "GET"])
def gameservers_live():
    get_remote_ip()
    try:
        print("Responded to Gameserver event api call X")
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
        return jsonify({"current-event": {}, "status": {}, "id": "live", "message": "Warning msg 1"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-tex", message=f"Error in tex_get: {e}")


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
        return {"current-event": {"status": {"id": "live"}, "message": "Warning MSG 2"}} # Alpha 2 WARNING Msg text?!?!
        # return jsonify({"status": "success", "online": "true", "Version": "te-18f25613-36778-ue4-374f864b",
        #                "ProjectID": "F72FA5E64FA43E878DC72896AD677FB5",
        #                "DefaultFactoryName": "HttpNetworkReplayStreaming", "ServeMatchDelayInMin": "30.0f"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="general-services-tex", message=f"Error in services_tex: {e}")


@app.route("/api/v1/consent/eula2", methods=["PUT", "GET"])
def consent_eula():
    get_remote_ip()
    try:
        if request.method == "PUT":
            userid = request.cookies.get('bhvrSession')
            try:
                mongo.eula(userId=userid, get_eula=False, server=mongo_host, db=mongo_db, collection=mongo_collection)
                print("Responded to consent eula api call PUT")
                return jsonify({"isGiven": True})
            except TimeoutError:
                print("Timeout error")
                return jsonify({"status": "error"})
            except Exception as e:
                logger.graylog_logger(level="error", handler="general-consent-eula", message=f"Error in consent_eula: {e}")
        elif request.method == "GET":
            if request.cookies.get('bhvrSession') is None:
                return jsonify({"isGiven": True})
            userid = request.cookies.get('bhvrSession')
            is_given = mongo.eula(userId=userid, get_eula=True, server=mongo_host, db=mongo_db, collection=mongo_collection)
            if is_given:
                return jsonify({"isGiven": True})
            else:
                return jsonify({"isGiven": False})
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
        print("Responded to leaderboard getScores api call POST")
        logger.graylog_logger(level="info", handler="general-leaderboard-get-scores", message=f"Leaderboard getScores: {request.get_json()}")
        return jsonify({"playerID": "a-1-b-2", "PlayerName": "Hans", "Rank": 1, "Score": 10,  "Percentile": 1})
    else:
        try:
            print("Responded to leaderboard getScores api call GET")
            return jsonify({"data": []})
        except TimeoutError:
            print("Timeout error")
            return jsonify({"status": "error"})
        except Exception as e:
            logger.graylog_logger(level="error", handler="general-leaderboard-get-scores", message=f"Error in leaderboard_get_scores: {e}")
