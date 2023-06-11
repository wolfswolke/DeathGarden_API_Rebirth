"""

"""
# ------------------------------------------------------- #
# imports
# ------------------------------------------------------- #
from flask import Flask, send_from_directory, request, jsonify, abort
from threading import Thread
import os
import yaml
import graypy
import requests
import logging
import time

from logic.mongodb_handler import user_db_handler
from logic.time_handler import get_time


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
            print("No valid log level specified.")
    else:
        print("Graylog disabled. Not sending any Logs.")


def get_remote_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_addr = request.environ['REMOTE_ADDR']
    else:
        ip_addr = request.environ['HTTP_X_FORWARDED_FOR']
    print("New Connection from: " + ip_addr)
    return ip_addr


def steam_login_function(appid):
    try:
        steam_session_token = request.args.get('token')
        response = requests.get(
            'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                steam_api_key, steam_session_token, appid))
        steamid = response.json()["response"]["params"]["steamid"]
        # owner_id = response.json()["response"]["params"]["result"]["ownersteamid"]  # This is providerId

        userid, token = user_db_handler(steamid, mongo_host, mongo_db, mongo_collection)
        current_time, expire_time = get_time()

        graylog_logger("User {} logged in".format(steamid), "info")
        print("User {} logged in".format(steamid))
        # Read: Doc -> AUTH
        # You can copy and paste the JSON from the Auth Doc here. If you don't have a steam api key.
        # The Client does not validate this and just uses it.
        return jsonify({"preferredLanguage": "en", "friendsFirstSync": {"steam": True}, "fixedMyFriendsUserPlatformId":
            {"steam": True}, "id": userid, "provider": {"providerId": steamid, "providerName": "steam", "userId":
            userid}, "providers": [{"providerName": "steam", "providerId": steamid}], "friends": [], "triggerResults":
                            {"success": [], "error": []}, "tokenId": userid, "generated": current_time,
                        "expire": expire_time,
                        "userId": userid, "token": token})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


app = Flask(__name__)


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


@app.route("/metrics/client/event", methods=["POST"])
def receive_event():
    get_remote_ip()
    try:
        print("Responded to Metrics api call POST")
        data = request.get_json()
        graylog_logger(data, "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/metrics/httplog/event", methods=["POST"])
def metrics_httplog_event():
    get_remote_ip()
    try:
        data = request.get_json()
        graylog_logger(data, "info")
        return jsonify({"status": "success"})
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


@app.route("/api/v1/gameDataAnalytics", methods=["POST"])
def analytics_post():
    get_remote_ip()
    try:
        print("Responded to analytics api call POST")
        data = request.get_json()
        graylog_logger(data, "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/gameDataAnalytics/batch", methods=["POST"])
def analytics_batch_post():
    get_remote_ip()
    try:
        print("Responded to analytics batch api call POST")
        data = request.get_json()
        graylog_logger(data, "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = get_remote_ip()
    user_agent = request.headers.get('User-Agent')
    print("####################################################")
    print("USER AGENT: " + user_agent)
    print("####################################################")

    if user_agent.startswith("TheExit/++UE4+Release-4.21-CL-0 Windows"):
        return_val = steam_login_function(555440)
        return return_val

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function(854040)
        return return_val

    else:
        graylog_logger("Unauthorized User Agent {} connected from IP {}".format(user_agent, ip), "error")
        abort(401, "Unauthorized")


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


@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    get_remote_ip()
    try:
        print("Responded to modifiers api call GET")
        return jsonify({"status": "success", "modifiers": []})  # Don't know. Added as Placeholder.
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



# Logging
@app.route("/api/v1/extensions/quitters/getQuitterState", methods=["POST"])
def get_quitter_state():
    get_remote_ip()
    try:
        print("Responded to get quitter state api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


# Logging
@app.route("/api/v1/extensions/progression/initOrGetGroups", methods=["POST"])
def extension_progression_init_or_get_groups():
    get_remote_ip()
    try:
        print("Responded to extension progression init or get groups api call POST")
        print(request.get_json())
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


# Logging
@app.route("/api/v1/me/richPresence", methods=["POST"])
def me_rich_presence():
    get_remote_ip()
    try:
        print("Responded to me rich presence api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    get_remote_ip()
    try:
        print("Responded to moderation check username api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success",
                        "isAllowed": "true"})  # CLIENT: {"userId": "ID-ID-ID-ID-SEE-AUTH",	"username": "Name-Name-Name"}
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


# Logging for Server Events
@app.route("/metrics/server/event", methods=["POST"])
def metrics_server_event():
    get_remote_ip()
    try:
        print("Responded to metrics server event api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


# [Backend]
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


@app.route("/te-18f25613-36778-ue4-374f864b/catalog", methods=["GET"])
def catalog_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    get_remote_ip()
    try:
        print("Responded to achievements api call GET")
        return jsonify({"status": "success", "achievements": []})  # Don't know. Added as Placeholder.
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


@app.route("/api/v1/players/ban/status", methods=["GET"])
def ban_status():
    get_remote_ip()
    try:
        print("Responded to ban status api call GET")
        return jsonify({"banned": "false"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/wallet/currencies", methods=["GET"])
def wallet_currencies():
    get_remote_ip()
    try:
        print("Responded to wallet currencies api call GET")
        return jsonify({"status": "success", "currencies": "EUR"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    get_remote_ip()
    try:
        print("Responded to Inventory Unlocik Speical Items event api call POST")
        graylog_logger(request.get_json(), "info")
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/crashreport/unreal/CrashReporter/CheckReport", methods=["POST"])
def crashreporter_check_report():
    get_remote_ip()
    try:
        print("Responded to crashreporter check report api call POST")
        # TODO: Add Crashreporter
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/utils/contentVersion/latest/2.2", methods=["GET"])
def content_version_latest():
    get_remote_ip()
    try:
        print("Responded to content cversion api call GET")
        return jsonify({{
            "availableVersions": {
                "10.0.19045.1.256live": "te-18f25613-36778-ue4-374f864b",
                "3.3.0_241792live": "te-f9b4768a-26590-ue4-cefc1aee",
                "3.3.0_244688live": "3.3.0_244688live-1573508813", }}})
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


@app.route("/api/v1/players/me/splinteredstates/ProgressionGroups", methods=["GET"])
def progression_groups():
    get_remote_ip()
    try:
        print("Responded to progression groups api call GET")
        return jsonify({"status": "success", "progressionGroups": [1]})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    get_remote_ip()
    try:
        print("Responded to progression experience api call POST")
        print(request.get_json())
        # graylog_logger(request.get_json(), "info")
        return jsonify({"groupExperiences":[{"objectId":"HuntersGroup","experience":1245,"version":2},{"objectId":"RunnersGroup","experience":512,"version":1},{"objectId":"RunnerCharacter1","experience":2584,"version":5},{"objectId":"RunnerCharacter2","experience":9552,"version":4},{"objectId":"RunnerCharacter3","experience":8885,"version":9},{"objectId":"RunnerCharacter4","experience":4218,"version":8},{"objectId":"RunnerCharacter5","experience":9953,"version":6},{"objectId":"HunterCharacter1","experience":2222,"version":8},{"objectId":"HunterCharacter2","experience":6541,"version":2},{"objectId":"HunterCharacter3","experience":6634,"version":7},{"objectId":"HunterCharacter4","experience":2112,"version":5},{"objectId":"HunterCharacter5","experience":1414,"version":6}]})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger("API ERROR: " + str(e), "error")


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    try:
        t = Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            time.sleep(100)
    except (KeyboardInterrupt, SystemExit):
        print('Received keyboard interrupt, quitting threads.')
        graylog_logger("Api shutting down do to keyboard interrupt.", "info")


# ------------------------------------------------------- #
# global variables
# ------------------------------------------------------- #

config = load_config()
use_graylog = config['graylog']['use']
graylog_server = config['graylog']['host']
steam_api_key = config['steam']['api_key']
mongo_host = config['mongodb']['host']
mongo_db = config['mongodb']['db']
mongo_collection = config['mongodb']['collection']

# ------------------------------------------------------- #
# main
# ------------------------------------------------------- #
setup_graylog()
keep_alive()
