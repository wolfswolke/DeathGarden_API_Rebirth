import time

from flask_definitions import *
import requests
from logic.mongodb_handler import mongo
from logic.time_handler import get_time

global steam_api_key, mongo_db, mongo_collection, mongo_host


def steam_login_function():
    try:
        steam_session_token = request.args.get('token')
        appid = 555440
        response = requests.get(
            'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                steam_api_key, steam_session_token, appid))
        if response.json() == {"response": {"error": {"errorcode": 102, "errordesc": "Ticket for other app"}}}:
            appid = 854040
            response = requests.get(
                'https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/?key={}&ticket={}&appid={}'.format(
                    steam_api_key, steam_session_token, appid))

        steamid = response.json()["response"]["params"]["steamid"]
        # owner_id = response.json()["response"]["params"]["result"]["ownersteamid"]  # This is providerId

        userid, token = mongo.user_db_handler(steamid, mongo_host, mongo_db, mongo_collection)
        current_time, expire_time = get_time()

        logger.graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(steamid))
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
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="steam_login", message=e)


# This works
@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = check = check_for_game_client("strict")  # ToDo: Change when cookie validation is added.
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    user_agent = request.headers.get('User-Agent')
    if user_agent.startswith("TheExit/++UE4+Release-4.2"):
        if request.args.get(
                'token') == "140000007B7B7B7B02000000E3FA3952010010017B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B":
            return_val = jsonify(
                {"preferredLanguage": "en", "friendsFirstSync": {"steam": True}, "fixedMyFriendsUserPlatformId":
                    {"steam": True}, "id": "aaaa", "provider": {"providerId": "aaaa", "providerName": "steam", "userId":
                    "aaaa"}, "providers": [{"providerName": "steam", "providerId": "aaaa"}], "friends": [],
                 "triggerResults":
                     {"success": [], "error": []}, "tokenId": "aaaa", "generated": 1687197541,
                 "expire": 1887197541,
                 "userId": "aaaa", "token": "aaaa"})
            return_val.set_cookie("bhvrSession", return_val.json["id"])
            return return_val
        try:
            return_val = steam_login_function()
            return_val.set_cookie("bhvrSession", return_val.json["id"])
            return return_val
        except Exception as e:
            logger.graylog_logger(level="error", handler="steam_login", message=e)
            abort(401, "Unauthorized")

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function()
        return_val.set_cookie("bhvrSession", return_val.json["id"])
        return return_val

    else:
        logger.graylog_logger(level="error", handler="steam_login", message={"text": "Access denied to User Agent",
                                                                             "User-Agent": user_agent, "IP": ip})
        abort(401, "Unauthorized")


# Dont know if this works
@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    userid = request.cookies.get("bhvrSession")
    steamid, token = mongo.get_data_with_list(login=userid, login_steam=False,
                                              items={"token", "steamid"}, server=mongo_host, db=mongo_db,
                                              collection=mongo_collection)
    try:
        return jsonify({"TokenId": token, "UserId": userid, "RoleIds": ["755D4DFE-40DA1512-B01E3D8C-FF3C8D4D",
                                                                        "C50FFFBF-46866131-82F45890-651797CE"]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=e)


# This works
@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        request_var = request.get_json()
        userid = request_var["userId"]
        username = request_var["username"]
        logger.graylog_logger(level="info", handler="moderation_check_username", message=request.get_json())

        steamid, token = mongo.get_data_with_list(login=userid, login_steam=False,
                                                items={"token", "steamid"}, server=mongo_host, db=mongo_db,
                                                collection=mongo_collection)
        if steamid is None:
            time.sleep(1)
            request_var = request.get_json()
            userid = request_var["userId"]
            username = request_var["username"]
            steamid, token = mongo.get_data_with_list(login=userid, login_steam=False,
                                                      items={"token", "steamid"}, server=mongo_host, db=mongo_db,
                                                      collection=mongo_collection)

        return jsonify({"Id": userid, "Token": token,
                        "Provider": {"ProviderName": username,
                                     "ProviderId": steamid}})  # CLIENT:{"userId": "ID-ID-ID-ID-SEE-AUTH",	"username": "Name-Name-Name"}
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_username", message=e)


# Doesn't work
@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="user_handling_progression_experience", message=request.get_json())
        return jsonify({"List": [
            {"ObjectId": "PlayerProgression", "SchemaVersion": 11122233344, "Version": 11122233345,
             "Data": {"ObjectId": "PlayerProgression", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233345, "Version": 11122233345,
             "Data": {"ObjectId": "Runner.Smoke", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Ghost", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Ink", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Sawbones", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Switch", "Experience": 100, "Version": 1}},
            {"ObjectId": "RunnerProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Runner.Dash", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Inquisitor", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Stalker", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Poacher", "Experience": 100, "Version": 1}},
            {"ObjectId": "HunterProgression", "SchemaVersion": 11122233346, "Version": 11122233346,
             "Data": {"ObjectId": "Hunter.Mass", "Experience": 100, "Version": 1}}
        ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="progression_experience", message=e)


@app.route("/api/v1/extensions/challenges/getChallenges", methods=["POST"])
def challenges_get_challenges():
    # client: {"data":{"userId":"619d6f42-db87-4f3e-8dc9-3c9995613614","challengeType":"Daily"}}
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        response = request.get_json()
        challenge_type = response["data"]["challengeType"]
        if challenge_type == "Weekly":
            return jsonify({"Challenges": ["ARBDamage_HunterWeekly", "AssaultRifleWins_HunterWeekly",
                                           "BleedOut_HunterWeekly", "BleedOut_RunnerWeekly", "Damage_HunterWeekly",
                                           "Double_HunterWeekly", "ActivateDrones", "Efficient_HunterWeekly",
                                           "Emotional_HunterWeekly", "Emotional_RunnerWeekly", "Greed_HunterWeekly",
                                           "Greed_RunnerWeekly", "Headshot", "HuntingShotgun_HunterWeekly",
                                           "InDenial_HunterWeekly", "LMGWins_HunterWeekly", "Hunter_WeeklyMines_Name",
                                           "Mines_RunnerWeekly", "Reveals_HunterWeekly", "RingOut_HunterWeekly",
                                           "Shields_RunnerWeekly", "ShotgunDowns_HunterWeekly", "Speed_HunterWeekly",
                                           "Speed_RunnerWeekly", "Stuns_RunnerWeekly", "Turrets_HunterWeekly",
                                           "Turrets_RunnerWeekly", "BleedOut_RunnerWeekly", "Wasteful_HunterWeekly",
                                           "Wasteful_RunnerWeekly", "WUP_HunterWeekly", "WUP_RunnerWeekly"]})
        elif challenge_type == "Daily":
            return jsonify({"Challenges": ["Daily_Domination_Hunter", "Daily_Domination_Runner"]})
        else:
            return jsonify({"status": "error"})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="getChallanges", message=e)


@app.route("/api/v1/extensions/challenges/executeChallengeProgressionOperationBatch", methods=["POST"])
def challenges_execute_challenge_progression_operation_batch():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="logging_executeChallengeProgressionOperationBatch",
                              message=request.get_json())
        return jsonify({"Id": "AssaultRifleWins_HunterWeekly", "Type": 2, "Title": "Hunter_DroneCharger_Name",
                        "Body": "Hunter_DroneCharger_DESC", "Progress": 1, "ValueToReach": 10, "TimeLeft": 1440000000,
                        "ShouldShowCompleteAnimation": True, "Rewards":
                            [{"Type": "Weekly", "Id": "C90F72FC4D61B1F2FBC73F8A4685EA41", "Amount": 1.0,
                              "Claimed": False}]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_executeChallengeProgressionOperationBatch",
                              message=e)


# idk dont think it works
@app.route("/api/v1/inventories", methods=["GET"])
def inventories():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        page = request.args.get('page', default=0, type=int)
        limit = request.args.get('limit', default=500, type=int)
        userid = request.cookies.get('bhvrSession')
        if page == 0:
            return jsonify({"Code": 200, "Message": "OK", "Data": {"PlayerId": userid, "Inventory": [
                {"ObjectId": "56B7B6F6-473712D0-B7A2F992-BB2C16CD", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "759E44DD-469C2841-75C2D6A1-AB0B0FA7", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "EF96A202-49884D43-7B87A6A4-BDE81B7F", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "755D4DFE-40DA1512-B01E3D8C-FF3C8D4D", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "CCA2272D-408ED953-87F017BE-D437FF9A", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "C50FFFBF-46866131-82F45890-651797CE", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "606129DC-45AB9D16-B69E2FA5-C99A9835", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "234FFD46-4C55514B-6C1E7386-45993CAA", "Quantity": 1, "LastUpdateAt": 16873773050},
                {"ObjectId": "0EA4B7BD-456E322E-E1F0E1BD-6D92F269", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "51595917-43CBF0B5-7EC6FEB3-341960D6", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "08DC38B6-470A7A5B-0BA025B9-6279DAA8", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "7902D836-470BBB49-DE9B9D97-F17C9DB5", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "1069E6DF-40AB4CAE-F2AF03B4-FD60BB22", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "5998C1C5-48AB7BDA-80C87295-F2764C5D", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "F055513D-48AACBAC-280B2AA0-0A984180", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "EDB6D6B7-42023AE6-1AD8718C-AC073C0E", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "1098BEE2-41B1515B-44013A87-EDB16BDC", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "973C9176-404A29F9-26D13BAC-B76A2425", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "50D3005B-437066E4-C4D99F93-97CF1B0B", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "B83A141A-45FB8D96-D48A5185-CD607AA3", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "9281A7AB-4EE28B4F-B6341886-DFD50391", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "4886DDC4-46B96FEE-1255D6A2-AB114B0D", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "0C6D2A46-48B95C22-64312783-F977F211", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "C215B81F-4E421961-03ECE989-49892499", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "30363336-4217BE70-33C637B7-EE7D9CE8", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "5889A14A-44DEC8EA-D019F69C-FD3C5A44", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "DA7C176F-48525599-C9477C95-137C7369", "Quantity": 1, "LastUpdateAt": 1687377305}
            ], "NextPage": 1}})
        elif page == 1:
            return jsonify({"Code": 200, "Message": "OK", "Data": {"PlayerId": userid, "Inventory": [
                {"ObjectId": "DA7C176F-48525599-C9477C95-137C7369", "Quantity": 1, "LastUpdateAt": 1687377305},
                {"ObjectId": "C1672541-4A4B16B9-AD557C9E-E865D113", "Quantity": 1, "LastUpdateAt": 1687377305}
            ], "NextPage": 0}})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="inventories", message=e)


# idk if this works
@app.route("/api/v1/players/me/splinteredstates/ProgressionGroups", methods=["GET"])
def progression_groups():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        userid = request.headers.get("bhvrSession")
        #  This is the real code but need to build this first
        # return jsonify({"UserId": userid, "StateName": "Fstring", "Segment": "Fstring", "ObjectId": "Fstring",
        #                "Version": 1111, "schemaVersion": 1111, "Data": {}})
        return jsonify({"List": [{"ObjectId": "C50FFFBF-46866131-82F45890-651797CE",
                                  "SchemaVersion": 11111111,
                                  "Version": 11111111,
                                  "Data":
                                      [{"Level": 5, "Ratio": 0.111}]},
                                 {"ObjectId": "755D4DFE-40DA1512-B01E3D8C-FF3C8D4D",
                                  "SchemaVersion": 11111111,
                                  "Version": 11111111,
                                  "Data":
                                      [{"Level": 5, "Ratio": 0.111}]}
                                 ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ProgressionGroups", message=e)


# This works
@app.route("/api/v1/players/ban/status", methods=["GET"])
def ban_status():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    login_cookie = request.cookies.get("bhvrSession")
    try:
        time.sleep(0.5)
        ban_data = mongo.get_data_with_list(login=login_cookie, login_steam=False,
                                            items={"is_banned", "ban_reason", "ban_start", "ban_expire"},
                                            server=mongo_host, db=mongo_db, collection=mongo_collection)
        if ban_data == None:
            return jsonify({"status": "error"})
        elif ban_data["is_banned"] == True:
            return jsonify({"IsBanned": ban_data["is_banned"], "BanInfo": {"BanPeriod": 10,
                                                                           "BanReason": ban_data["ban_reason"],
                                                                           "BanStart": ban_data["ban_start"],
                                                                           "BanEnd": ban_data["ban_expire"],
                                                                           "Confirmed": False, "Pending": False}})
        elif ban_data["is_banned"] == False:
            return jsonify({"IsBanned": ban_data["is_banned"], "BanInfo": {"BanPeriod": 0,
                                                                           "BanReason": "None",
                                                                           "BanStart": 0,
                                                                           "BanEnd": 0,
                                                                           "Confirmed": False, "Pending": False}})
        else:
            return jsonify({"status": "error"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ban_status", message=e)


# broken. no need to fix... OG DG endpoint. Not needed.
@app.route("/api/v1/players/ban/getbaninfo", methods=["GET"])
def get_ban_info():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify({"BanPeriod": None, "BanReason": None, "BanStart": None, "BanEnd": None,
                        "Confirmed": False})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="ban_status", message=e)


# This works
@app.route("/api/v1/wallet/currencies", methods=["GET"])
def wallet_currencies():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        currencies = mongo.get_data_with_list(login=request.cookies.get("bhvrSession"), login_steam=False,
                                              items={"currency_blood_cells", "currency_iron", "currency_ink_cells"},
                                              server=mongo_host, db=mongo_db, collection=mongo_collection)
        return jsonify({"List": [{"Currency": "CurrencyA", "Balance": currencies["currency_iron"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "CurrencyB", "Balance": currencies["currency_blood_cells"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "CurrencyC", "Balance": currencies["currency_ink_cells"],
                                  "CurrencyGroup": "SoftCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "HARD_CURRENCY", "Balance": 6969,
                                  "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"},
                                 {"Currency": "PROGRESSION_CURRENCY", "Balance": 10000,
                                  "CurrencyGroup": "HardCurrencyGroup", "LastRefillTimeStamp": "1684862187"}]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# Does not work. Old DG endpoint. Not needed.
@app.route("/api/v1/wallet/currencies/PROGRESSION_CURRENCY", methods=["GET"])
def wallet_currencies_progression():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify([{"Currency": 1, "Amount": 10}, {"Currency": 2, "Amount": 10}, {"Currency": 3, "Amount": 10}])
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# Dont know if this works. Dont think it does.
@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        userid = request.cookies.get("bhvrSession")
        return jsonify({"UserId": userid, "StateName": "", "Segment": "", "List": [
            {"ObjectId": "EFAB89E6465D1163D62A07B11048F2B6", "Version": 11, "SchemaVersion": 11, "Data": {}}
        ]})
        # This works but lemme test smthing...
        return jsonify({"gameName": "Deathgarden: BLOODHARVEST", "achievements":
            [{"apiname": "EFAB89E6465D1163D62A07B11048F2B6", "achieved": 1, "unlocktime": 1587140058},
             {"apiname": "2CAEBB354D506D7C43B941BC1DA775A0", "achieved": 1, "unlocktime": 1586792410},
             {"apiname": "E51981B946BEE3D45C5C41B2FCFF310B", "achieved": 1, "unlocktime": 1586788872},
             {"apiname": "AAD05B9D46471DC811BBE0BA91916AB7", "achieved": 1, "unlocktime": 1586788872},
             {"apiname": "BA2D4A5445CB70276A8F5D9E1AFCE080", "achieved": 1, "unlocktime": 1586788872}]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="Achievment_handler", message=e)


# Does not work
@app.route("/api/v1/messages/count", methods=["GET"])
def messages_count():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        return jsonify({"Count": 1})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_count", message=e)


@app.route("/api/v1/messages/list", methods=["GET"])
def messages_list():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        limit = request.args.get("limit")
        output = json.load(open(os.path.join(app.root_path, "json", "placeholders", "messages.json"), "r"))
        return jsonify(output)
        return jsonify({"messages": []})  # from dbd
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_list", message=e)


# Temp response.
@app.route("/moderation/check/chat", methods=["POST"])
def moderation_check_chat():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        data = request.get_json()
        userid = data["userId"]
        language = data["language"]
        message = data["message"]
        # Why should we care? Can we get in trouble if we don't?
        return jsonify({"status": "success", "result": "OK"})  # Testing stuff
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_chat", message=e)


# This is intently broken. If this works the game crashes in matchmaking.
@app.route("/api/v1/extensions/progression/initOrGetGroups", methods=["POST"])
def extension_progression_init_or_get_groups():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="logging_initOrGetGroups", message=request.get_json())
        # Client sends: {"data":{"skipProgressionGroups":false,"skipMetadataGroups":false,"playerName":"Steam-Name-Here"}}
        # The client cant understand CharacterId for some reason??? But if this is removed the game doesn't load the
        # "Choose Hunter or Runner" screen.
        return jsonify({
            "ProgressionGroups": [
                {
                    "ObjectId": "755D4DFE-40DA1512-B01E3D8C-FF3C8D4D",
                    "Version": 1,
                    "SchemaVersion": 1.1,
                    "Data": {"Experience": {"Level": 11, "CurrentExperience": 2, "ExperienceToReach": 30}},
                },
                {
                    "ObjectId": "C50FFFBF-46866131-82F45890-651797CE",
                    "Version": 1,
                    "SchemaVersion": 1.1,
                    "Data": {"Experience": {"Level": 21, "CurrentExperience": 12, "ExperienceToReach": 30}},
                }
            ],
            "MetadataGroups": [
                {
                    "ObjectId": "755D4DFE-40DA1512-B01E3D8C-FF3C8D4D",
                    "Version": 1,
                    "SchemaVersion": 1.1,
                    "Data": {"CharacterId": {"TagName": "Runner.Sawbones"},
                             "Equipment": ["Primary Weapon", "Bonus 1", "Bonus 2", "Perk 1",
                                           "Perk 2"],
                             "EquippedPerks": ["BE1C0D4C-4CE08611-22BE22B2-736D9091",
                                               "F2768C45-41C8262E-FF4922B3-72AB7306"],
                             "EquippedPowers": ["C8AF3D53-4973F82F-ADBB40BD-A96F9DCD"],
                             "EquippedWeapons": ["4E171BD1-4FF98ED4-3A7AFAB5-7FE55578"],
                             "EquippedBonuses": ["109BC590-4DC1272D-70822EBA-79CC85B1",
                                                 "54B3EF79-4FCB0643-C4644FA1-5BEF31D5"]}
                },
                {
                    "ObjectId": "C50FFFBF-46866131-82F45890-651797CE",
                    "Version": 1,
                    "SchemaVersion": 1.1,
                    "Data": {"CharacterId": "{AAAA-BBBBB-2222-33333}",
                             "Equipment": ["Primary Weapon", "Bonus 1", "Bonus 2", "Perk 1",
                                           "Perk 2", "Ability01", "Ability02", "Ability03","Sidearm"],
                             "EquippedPerks": ["7CE5AFBF-459102E5-728DCDAA-6F88C0F1",
                                               "2DBF9B11-4B82A639-40936396-CBA68BCD"],
                             "EquippedPowers": ["10A8C667-45801664-6E2EFA94-52E3141A",
                                                "08DC38B6-470A7A5B-0BA025B9-6279DAA8",
                                                "51595917-43CBF0B5-7EC6FEB3-341960D6"],
                             "EquippedWeapons": ["36466540-42433114-08F6A0BD-4DCE05BD",
                                                 "307A0B13-417737DE-D675309F-8B978AB8"],
                             "EquippedBonuses": ["791F12E0-47DA9E26-E246E385-9C3F587E",
                                                 "8A5BF227-4640C2F2-3EF3C996-A6F6404D"]}
                }
            ]
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_initOrGetGroups", message=e)


# dont know if this works. Hope it does.
@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="unknown_unlockSpecialItems", message=request.get_json())
        return jsonify({"UnlockedItems": ["9F54DE7A-4E15935B-503850A1-27B0A2A4"]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="unknown_unlockSpecialItems", message=e)


@app.route("/api/v1/extensions/challenges/getChallengeProgressionBatch", methods=["POST"])
def challenges_get_challenge_progression_batch():
    check = check_for_game_client("strict")
    if not check:
        return jsonify({"message": "Endpoint not found"}), 404
    try:
        logger.graylog_logger(level="info", handler="logging_getChallengeProgressionBatch",
                              message=request.get_json())
        # MirrorsExtModelGetChallengeProgressionBatchResponse -> TArray MirrorsExtModelChallengeProgressionOperation
        return jsonify({"ProgressionBatch": [{"ChallengeId": "", "OperationName": "", "OperationData": []}]})
    except TimeoutError:
        return jsonify({"status": "error"})

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getChallengeProgressionBatch", message=e)
