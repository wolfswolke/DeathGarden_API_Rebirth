from flask_definitions import *
import requests
from logic.mongodb_handler import user_db_handler
from logic.time_handler import get_time

global steam_api_key, mongo_db, mongo_collection, mongo_host


def steam_login_function():
    try:
        steam_session_token = request.args.get('token')
        appid = 555440
        response = requests.get(
            'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                steam_api_key, steam_session_token, appid))
        if response.json() == {"response":{"error":{"errorcode":102,"errordesc":"Ticket for other app"}}}:
            appid = 854040
            response = requests.get(
                'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                    steam_api_key, steam_session_token, appid))

        steamid = response.json()["response"]["params"]["steamid"]
        # owner_id = response.json()["response"]["params"]["result"]["ownersteamid"]  # This is providerId

        userid, token = user_db_handler(steamid, mongo_host, mongo_db, mongo_collection)
        current_time, expire_time = get_time()

        graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(steamid))
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
        graylog_logger(level="error", handler="steam_login", message=str(e))


@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = get_remote_ip()
    user_agent = request.headers.get('User-Agent')
    print("####################################################")
    print("USER AGENT: " + user_agent)
    print("####################################################")

    if user_agent.startswith("TheExit/++UE4+Release-4.2"):
        try:
            return_val = steam_login_function()
            return return_val
        except Exception as e:
            graylog_logger(level="error", handler="steam_login", message=str(e))
            abort(401, "Unauthorized")

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function()
        return return_val

    else:
        graylog_logger(level="error", handler="steam_login", message={"text": "Access denied to User Agent", "User-Agent": user_agent, "IP": ip})
        abort(401, "Unauthorized")


@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "modifiers": []})  # Don't know. Added as Placeholder.
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="modifiers_me", message=str(e))


@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    get_remote_ip()
    try:
        graylog_logger(level="info", handler="moderation_check_username", message=request.get_json())
        return jsonify({"status": "success",
                        "isAllowed": "true"})  # CLIENT: {"userId": "ID-ID-ID-ID-SEE-AUTH",	"username": "Name-Name-Name"}
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="moderation_check_username", message=str(e))


@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    get_remote_ip()
    try:
        # graylog_logger(request.get_json(), "info")
        return jsonify({'groupExperiences': [{'objectId': 'PlayerProgression', 'experience': 0.57, 'version': 1}, {'objectId': 'RunnerProgression', 'experience': 0.555, 'version': 1}, {'objectId': 'HunterProgression', 'experience': 0.67, 'version': 1}]})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="progression_experience", message=str(e))


@app.route("/api/v1/extensions/challenges/getChallenges", methods=["POST"])
def challenges_get_challenges():
    get_remote_ip()
    try:
        print("Responded to challenges get challenges api call POST")
        graylog_logger(level="info", handler="challenges_get_challenges", message=request.get_json())
        return jsonify({"status": "success"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="getChallanges", message=str(e))


@app.route("/api/v1/inventories", methods=["GET"])
def inventories():
    get_remote_ip()
    try:
        print("Responded to inventories api call GET")
        return jsonify({})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="inventories", message=str(e))


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
        graylog_logger(level="error", handler="ProgressionGroups", message=str(e))


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
        graylog_logger(level="error", handler="ban_status", message=str(e))


@app.route("/api/v1/wallet/currencies", methods=["GET"])
def wallet_currencies():
    get_remote_ip()
    try:
        print("Responded to wallet currencies api call GET")
        return jsonify({"currencies": "EUR"})
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="currencies", message=str(e))


@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    get_remote_ip()
    try:
        return jsonify({"status": "success", "achievements": []})  # Don't know. Added as Placeholder.
    except TimeoutError:
        print("Timeout error")
        return jsonify({"status": "error"})
    except Exception as e:
        graylog_logger(level="error", handler="Achievment_handler", message=str(e))
