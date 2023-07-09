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
        return jsonify({"availableVersions": {"5.5.0_529855dev": "5.5.0_529855dev-1644265094",
                                              "6.6.0_1091934dev": "6.6.0_1091934dev-1680028709",
                                              "6.7.0_1244914dev": "6.7.0_1244914dev-1686157047",
                                              "7.0.0_1269265dev": "7.0.0_1269265dev-1688489919",
                                              "7.1.0_1273986dev": "7.1.0_1273986dev-1688568602",
                                              "7.1.0_1274117dev": "7.1.0_1274117dev-1688574101",
                                              "7.1.0_1274124dev": "7.1.0_1274124dev-1688574720",
                                              "7.1.0_1274234dev": "7.1.0_1274234dev-1688579224",
                                              "7.1.0_1274943dev": "7.1.0_1274943dev-1688657816",
                                              "7.1.0_1275139dev": "7.1.0_1275139dev-1688665451",
                                              "7.1.0_1275191dev": "7.1.0_1275191dev-1688667321",
                                              "7.1.0_1275245dev": "7.1.0_1275245dev-1688668372",
                                              "7.1.0_1275256dev": "7.1.0_1275256dev-1688669209",
                                              "7.2.0_1269696dev": "7.2.0_1269696dev-1688511907",
                                              "7.2.0_1274208dev": "7.2.0_1274208dev-1688578186",
                                              "7.2.0_1274225dev": "7.2.0_1274225dev-1688578617",
                                              "7.2.0_1274762dev": "7.2.0_1274762dev-1688651417",
                                              "7.2.0_1274768dev": "7.2.0_1274768dev-1688651827",
                                              "7.2.0_1274865dev": "7.2.0_1274865dev-1688655571",
                                              "7.2.0_1274930dev": "7.2.0_1274930dev-1688656773",
                                              "7.2.0_1275015dev": "7.2.0_1275015dev-1688660110",
                                              "7.2.0_1275045dev": "7.2.0_1275045dev-1688661324",
                                              "7.2.0_1275275dev": "7.2.0_1275275dev-1688669004",
                                              "7.2.0_1275518dev": "7.2.0_1275518dev-1688678079",
                                              "7.2.0_1275550dev": "7.2.0_1275550dev-1688678716",
                                              "7.3.0_1274067dev": "7.3.0_1274067dev-1688571863",
                                              "7.3.0_1274074dev": "7.3.0_1274074dev-1688572269",
                                              "7.3.0_1275510dev": "7.3.0_1275510dev-1688678288",
                                              "7.4.0_1248745dev": "7.4.0_1248745dev-1686588297",
                                              "7.5.0_1249994dev": "7.5.0_1249994dev-1686681980",
                                              "9999.0.0_609872dev": "9999.0.0_609872dev-1660659418",
                                              "9999.10.0_1265497dev": "9999.10.0_1265497dev-1687899211",
                                              "9999.11.0_657407dev": "9999.11.0_657407dev-1669385085",
                                              "9999.12.0_694236dev": "9999.12.0_694236dev-1676299372",
                                              "9999.13.0_1091319dev": "9999.13.0_1091319dev-1680005487",
                                              "9999.14.0_762536dev": "9999.14.0_762536dev-1677681328",
                                              "9999.15.0_763076dev": "9999.15.0_763076dev-1677688243",
                                              "9999.16.0_877270dev": "9999.16.0_877270dev-1677704562",
                                              "9999.17.0_1274055dev": "9999.17.0_1274055dev-1688571229",
                                              "9999.17.0_1274062dev": "9999.17.0_1274062dev-1688571650",
                                              "9999.17.0_1274136dev": "9999.17.0_1274136dev-1688575745",
                                              "9999.17.0_1274145dev": "9999.17.0_1274145dev-1688576013",
                                              "9999.17.0_1274226dev": "9999.17.0_1274226dev-1688579020",
                                              "9999.17.0_1274249dev": "9999.17.0_1274249dev-1688579726",
                                              "9999.17.0_1275007dev": "9999.17.0_1275007dev-1688660890",
                                              "9999.17.0_1275145dev": "9999.17.0_1275145dev-1688666088",
                                              "9999.17.0_1275180dev": "9999.17.0_1275180dev-1688666695",
                                              "9999.17.0_1275234dev": "9999.17.0_1275234dev-1688668154",
                                              "9999.17.0_1275240dev": "9999.17.0_1275240dev-1688668787",
                                              "9999.17.0_1275286dev": "9999.17.0_1275286dev-1688669831",
                                              "9999.17.0_1275312dev": "9999.17.0_1275312dev-1688670220",
                                              "9999.17.0_1275323dev": "9999.17.0_1275323dev-1688670523",
                                              "9999.17.0_1275398dev": "9999.17.0_1275398dev-1688673817",
                                              "9999.18.0_1269657dev": "9999.18.0_1269657dev-1688509288",
                                              "9999.18.0_1273987dev": "9999.18.0_1273987dev-1688568396",
                                              "9999.18.0_1273989dev": "9999.18.0_1273989dev-1688568812",
                                              "9999.18.0_1274127dev": "9999.18.0_1274127dev-1688574928",
                                              "9999.18.0_1274134dev": "9999.18.0_1274134dev-1688575537",
                                              "9999.18.0_1274392dev": "9999.18.0_1274392dev-1688588936",
                                              "9999.18.0_1274959dev": "9999.18.0_1274959dev-1688657611",
                                              "9999.18.0_1274961dev": "9999.18.0_1274961dev-1688658223",
                                              "9999.18.0_1275143dev": "9999.18.0_1275143dev-1688665667",
                                              "9999.18.0_1275165dev": "9999.18.0_1275165dev-1688666491",
                                              "9999.18.0_1275199dev": "9999.18.0_1275199dev-1688667115",
                                              "9999.18.0_1275200dev": "9999.18.0_1275200dev-1688667940",
                                              "9999.18.0_1275247dev": "9999.18.0_1275247dev-1688668583",
                                              "9999.18.0_1275271dev": "9999.18.0_1275271dev-1688669627",
                                              "9999.19.0_1091258dev": "9999.19.0_1091258dev-1679951263",
                                              "9999.2.0_481897dev": "9999.2.0_481897dev-1632318120",
                                              "9999.20.0_1092886dev": "9999.20.0_1092886dev-1680114849",
                                              "9999.21.0_1274992dev": "9999.21.0_1274992dev-1688658975",
                                              "9999.21.0_1275004dev": "9999.21.0_1275004dev-1688660446",
                                              "9999.3.0_478415dev": "9999.3.0_478415dev-1631543750",
                                              "9999.4.0_569535dev": "9999.4.0_569535dev-1652383024",
                                              "9999.5.0_1245806dev": "9999.5.0_1245806dev-1686163729",
                                              "9999.6.0_644076dev": "9999.6.0_644076dev-1666886965",
                                              "9999.7.0_638225dev": "9999.7.0_638225dev-1666023431",
                                              "9999.8.0_584495dev": "9999.8.0_584495dev-1657129066",
                                              "cauclair_7.3.0_0dev": "cauclair_7.3.0_0dev-1688497884",
                                              "fprevost_7.1.0_0dev": "fprevost_7.1.0_0dev-1688407952",
                                              "jescalante_7.3.0_0dev": "jescalante_7.3.0_0dev-1688673951",
                                              "jkfisera_7.1.0_0dev": "jkfisera_7.1.0_0dev-1688587429",
                                              "jkfisera_9999.17.0_0dev": "jkfisera_9999.17.0_0dev-1688578389",
                                              "m_4.4.0_402831dev": "m_4.4.0_402831dev-1614200535",
                                              "m_5.1.0_486821dev": "m_5.1.0_486821dev-1633535415",
                                              "m_5.2.0_501889dev": "m_5.2.0_501889dev-1637331411",
                                              "m_5.4.0_633895dev": "m_5.4.0_633895dev-1665499070",
                                              "m_5.4.1_689083dev": "m_5.4.1_689083dev-1675261407",
                                              "mcharron_7.0.0_0dev": "mcharron_7.0.0_0dev-1688493123"}})
        # return jsonify({"LatestSupportedVersion": "te-18f25613-36778-ue4-374f864b"})
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
