import sys
import time
from math import ceil

from flask_definitions import *
import requests
from logic.time_handler import get_time

global steam_api_key


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
            logger.graylog_logger(level="info", handler="steam_login",
                                  message="User {} logged in with SOFTLAUNCH".format(steamid))
            return jsonify({"status": "error"})

        steamid = response.json()["response"]["params"]["steamid"]
        userid, token = mongo.user_db_handler(steamid)
        current_time, expire_time = get_time()

        logger.graylog_logger(level="info", handler="steam_login", message="User {} logged in".format(steamid))
        # Read: Doc -> AUTH
        # You can copy and paste the JSON from the Auth Doc here. If you don't have a steam api key.
        # The Client does not validate this and just uses it.

        # if acc younger than cur + 1209600 ban
        # This is stupid... Why ban people for being new?
        user_data_response = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={steamid}")
        user_data = user_data_response.json()["response"]["players"][0]
        logger.graylog_logger(level="info", handler="steam_login", message=user_data)
        if user_data["communityvisibilitystate"] == 3:
            timecreated = user_data["timecreated"]
            if timecreated > current_time + 1209600:
                logger.graylog_logger(level="info",
                                      handler="steam_login",
                                      message=f"User {steamid} got banned for ban evasion.")
                mongo.write_data_with_list(login=userid,
                                           login_steam=False,
                                           items_dict={"is_banned": True,
                                                       "ban_reason": "Ban evasion detected.",
                                                       "ban_start": current_time,
                                                       "ban_expire": 1893459600})

        if dev_env == "true":
            get_challenge_ids_from_inventory(userid)
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


def get_init_or_get_groups(userid, request_data):
    data = {}
    skip_progression_groups = request_data["data"]["skipProgressionGroups"]
    skip_metadata_groups = request_data["data"]["skipMetadataGroups"]
    if not skip_progression_groups:
        Progression_HunterGroupA = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupA"})
        Progression_HunterGroupB = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupB"})
        Progression_HunterGroupC = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupC"})
        Progression_HunterGroupD = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"HunterGroupD"})
        Progression_RunnerGroupA = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupA"})
        Progression_RunnerGroupB = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupB"})
        Progression_RunnerGroupC = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupC"})
        Progression_RunnerGroupD = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupD"})
        Progression_RunnerGroupE = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupE"})
        Progression_RunnerGroupF = mongo.get_data_with_list(login=userid, login_steam=False,
                                                            items={"RunnerGroupF"})
        RunnerProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"RunnerProgression"})
        HunterProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"HunterProgression"})
        PlayerProgression = mongo.get_data_with_list(login=userid, login_steam=False,
                                                     items={"PlayerProgression"})

        data["progressionGroups"] = [
            {
                "version": 10,
                "objectId": "HunterGroupA",
                "data": {
                    "experience": Progression_HunterGroupA["HunterGroupA"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupB",
                "data": {
                    "experience": Progression_HunterGroupB["HunterGroupB"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupC",
                "data": {
                    "experience": Progression_HunterGroupC["HunterGroupC"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterGroupD",
                "data": {
                    "experience": Progression_HunterGroupD["HunterGroupD"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterProgression",
                "data": {
                    "experience": HunterProgression["HunterProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "PlayerProgression",
                "data": {
                    "experience": PlayerProgression["PlayerProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 646,
                "objectId": "RunnerGroupA",
                "data": {
                    "experience": Progression_RunnerGroupA["RunnerGroupA"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerGroupB",
                "data": {
                    "experience": Progression_RunnerGroupB["RunnerGroupB"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerGroupC",
                "data": {
                    "experience": Progression_RunnerGroupC["RunnerGroupC"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 36,
                "objectId": "RunnerGroupD",
                "data": {
                    "experience": Progression_RunnerGroupD["RunnerGroupD"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 3229,
                "objectId": "RunnerGroupE",
                "data": {
                    "experience": Progression_RunnerGroupE["RunnerGroupE"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 7,
                "objectId": "RunnerGroupF",
                "data": {
                    "experience": Progression_RunnerGroupF["RunnerGroupF"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            },
            {
                "version": 235,
                "objectId": "RunnerProgression",
                "data": {
                    "experience": RunnerProgression["RunnerProgression"]["experience"],
                    "metadata": [

                    ]
                },
                "schemaVersion": 1
            }
        ]
    if not skip_metadata_groups:
        data["metadataGroups"] = []

        last_played_faction = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_played_faction"})
        tutorial_completed = mongo.get_data_with_list(login=userid, login_steam=False, items={"tutorial_completed"})
        last_runner = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_runner"})
        last_hunter = mongo.get_data_with_list(login=userid, login_steam=False, items={"last_hunter"})
        hasPlayedDeathGarden1 = mongo.get_data_with_list(login=userid, login_steam=False,
                                                         items={"hasPlayedDeathGarden1"})
        characterCumulativeExperience = mongo.get_data_with_list(login=userid, login_steam=False,
                                                                 items={"ProfileMetaData"})["ProfileMetaData"][
            "characterCumulativeExperience"]

        Runner_List = ["RunnerGroupA", "RunnerGroupB", "RunnerGroupC", "RunnerGroupD", "RunnerGroupE", "RunnerGroupF"]
        Hunter_List = ["HunterGroupA", "HunterGroupB", "HunterGroupC", "HunterGroupD"]

        data["metadataGroups"] = [
            {
                "version": 342,
                "objectId": "PlayerMetadata",
                "data": {
                    "lastPlayedFaction": last_played_faction["last_played_faction"],
                    "shouldPlayWithoutContextualHelp": tutorial_completed["tutorial_completed"],
                    "lastPlayedRunnerId": {
                        "tagName": last_runner["last_runner"]
                    },
                    "lastPlayedHunterId": {
                        "tagName": last_hunter["last_hunter"]
                    },
                    "hasPlayedDeathGarden1": hasPlayedDeathGarden1["hasPlayedDeathGarden1"]
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "HunterMetadata",
                "data": [
                ],
                "schemaVersion": 1
            },
            {
                "version": 804,
                "objectId": "ProfileMetadata",
                "data": {
                    "characterCumulativeExperience": characterCumulativeExperience
                },
                "schemaVersion": 1
            },
            {
                "version": 2,
                "objectId": "RunnerMetadata",
                "data": [
                ],
                "schemaVersion": 1
            }
        ]

        for group in Runner_List + Hunter_List:
            group_data = mongo.get_data_with_list(login=userid, login_steam=False, items={group})[group]
            equippedPerks = group_data["EquippedPerks"]
            equippedWeapons = group_data["EquippedWeapons"]
            equipment = group_data["Equipment"]
            equippedBonuses = group_data["EquippedBonuses"]
            equippedPowers = group_data["EquippedPowers"]
            prestige = group_data["prestige"]
            if dev_env == "false":
                pickedChallenges = []
            else:
                pickedChallenges = group_data["pickedChallenges"]
            characterId = group_data["characterId"]
            equippedConsumables = group_data["equippedConsumables"]

            data["metadataGroups"].append({
                "version": 3,
                "objectId": group,
                "data": {
                    "equippedPerks": equippedPerks,
                    "equippedWeapons": equippedWeapons,
                    "equipment": equipment,
                    "equippedBonuses": equippedBonuses,
                    "pickedChallenges": pickedChallenges,
                    "equippedConsumables": equippedConsumables,
                    "characterId": characterId,
                    "equippedPowers": equippedPowers,
                    "prestigeLevel": prestige
                },
                "schemaVersion": 1
            })

    data["rewards"] = []
    return data


# This works
@app.route("/api/v1/auth/provider/steam/login", methods=["POST"])
def steam_login():
    # Read Doc\SteamAuth.md for more information
    ip = check_for_game_client("soft")
    user_agent = sanitize_input(request.headers.get('User-Agent'))
    request_token = sanitize_input(request.args.get('token'))
    if user_agent.startswith("TheExit/++UE4+Release-4.2"):
        if request_token == "140000007B7B7B7B02000000E3FA3952010010017B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B7B":
            userid, token = mongo.user_db_handler("Debug_session")
            current_time, expire_time = get_time()
            return_val = jsonify({"preferredLanguage": "en", "friendsFirstSync": {"steam": True},
                                  "fixedMyFriendsUserPlatformId":
                                      {"steam": True}, "id": userid,
                                  "provider": {"providerId": userid, "providerName": "steam", "userId":
                                      userid}, "providers": [{"providerName": "steam", "providerId": userid}],
                                  "friends": [],
                                  "triggerResults":
                                      {"success": [], "error": []}, "tokenId": userid, "generated": current_time,
                                  "expire": expire_time,
                                  "userId": userid, "token": token})
            session_cookie = session_manager.create_session(userid)
            return_val.set_cookie("bhvrSession", session_cookie)
            return return_val
        try:

            return_val = steam_login_function()
            session_cookie = session_manager.create_session(return_val.json["id"])
            print(f"Logged in with token: {session_cookie}", file=sys.stderr)
            return_val.set_cookie("bhvrSession", session_cookie)
            return return_val
        except Exception as e:
            logger.graylog_logger(level="error", handler="steam_login", message=e)
            abort(401, "Unauthorized")

    elif user_agent.startswith("game=TheExit, engine=UE4, version="):
        return_val = steam_login_function()
        session_cookie = session_manager.create_session(return_val.json["id"])
        return_val.set_cookie("bhvrSession", session_cookie)
        return return_val

    else:
        logger.graylog_logger(level="error", handler="steam_login", message={"text": "Access denied to User Agent",
                                                                             "User-Agent": user_agent, "IP": ip})
        abort(401, "Unauthorized")


# This works
@app.route("/api/v1/modifierCenter/modifiers/me", methods=["GET"])
def modifiers():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    data = mongo.get_data_with_list(login=userid, login_steam=False,
                                    items={"steamid", "token"})

    token = data["token"]
    steamid = data["steamid"]
    try:
        # Event modifiers
        # Just gonna leave this here for anyone that wants to rework it in the future.
        # {"modifiers":[{"id":"MainGameMode","startDate":1570122900,"endDate":1913057966,"duration":1913057966,"effects":{"matchGameMode":"MatchGameMode.HarvestYourExit.All","onlyForFaction":"None","experiencePercent":0,"currencyListPercent":[],"queueModifier":{"queueGroupModifiers":[{"groupName":"B","specifyPlayerCount":false}]}},"repeatDelays":[]},{"id":"SecondaryGameMode","startDate":1569160800,"endDate":2145934800,"duration":86400,"effects":{"matchGameMode":"MatchGameMode.HarvestYourExit.All","onlyForFaction":"None","experiencePercent":0,"currencyListPercent":[],"queueModifier":{"queueGroupModifiers":[{"groupName":"B","specifyPlayerCount":false}]}},"repeatDelays":[604800]}]}
        return jsonify({"Modifiers": []})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=e)


@app.route("/api/v1/modifierCenter/modifiers/<userid>", methods=["GET"])
def modifiers_userid(userid):
    # Same as above, but get for a person
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    #steamid, token = mongo.get_data_with_list(login=userid, login_steam=False,
    #                                          items={"token", "steamid"})
    try:
        # todo TEMP REMOVE
        users_with_dg1 = [
            "76561198129051713",
            "76561198076387733",
            "76561197960308924",
            "76561198838605143",
            "76561198375755382",
            "76561198190942526",
            "76561198085931811",
            "76561198804479305",
            "76561197987790181",
            "76561198051757391",
            "76561197987310750",
            "76561198811124309",
            "76561198275831683",
            "76561198331700778",
            "76561198064369535",
            "76561198069250881",
            "76561198059448904",
            "76561198143207619",
            "76561198069014976",
            "76561198140796510",
            "76561199169781285",
            "76561198124949660"
        ]
        data = mongo.get_data_with_list(login=userid, login_steam=False, items={"steamid", "hasPlayedDeathGarden1"})
        if not data["hasPlayedDeathGarden1"]:
            if data["steamid"] in users_with_dg1:
                mongo.write_data_with_list(login=userid, login_steam=False,
                                           items_dict={"hasPlayedDeathGarden1": True})
        return jsonify({"Modifiers": []})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="modifiers_me", message=e)


# This works
@app.route("/moderation/check/username", methods=["POST"])
def moderation_check_username():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        request_var = request.get_json()
        userid = sanitize_input(request_var["userId"])
        username = sanitize_input(request_var["username"])
        # This would be to censor usernames, but we don't need to do that.
        # Also not sure if this is the right response
        steam_id = mongo.get_data_with_list(login=userid, login_steam=False, items={"steamid"})["steamid"]
        developers = ["76561198124949660", "76561199169781285"]
        if steam_id in developers:
            username = "Dev: " + username
            return username
        return jsonify({
            "Username": username,
            "UserId": userid
        })
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_username", message=e)


# Doesn't work
# OG DG Endpoint
@app.route("/api/v1/progression/experience", methods=["POST"])
def progression_experience():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

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
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    # Removed because Challenges are still broken.
    if dev_env == "false":
        return jsonify({"status": "error"})

    try:
        response = request.get_json()
        challenge_type = sanitize_input(response["data"]["challengeType"])
        if challenge_type == "Weekly":
            return_data = new_challenge_handler.get_time_based_challenges(challenge_type="Weekly", userid=userid)
        elif challenge_type == "Daily":
            return_data = new_challenge_handler.get_time_based_challenges(challenge_type="Daily", userid=userid)
        else:
            logger.graylog_logger(level="error", handler="getChallenges",
                                  message=f"Unknown challenge type {challenge_type}")
            return jsonify({"status": "Unknown_Challenge_Type"})
        return jsonify({"challenges": return_data})

    except TimeoutError:
        return jsonify({"status": "TimeOutError"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="getChallenges", message=e)
        return jsonify({"status": "UnknownError"})


@app.route("/api/v1/extensions/challenges/executeChallengeProgressionOperationBatch", methods=["POST"])
def challenges_execute_challenge_progression_operation_batch():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    user_id = session_manager.get_user_id(session_cookie)
    try:
        data = request.get_json()
        userId = data["data"]["userId"]
        operations = data["data"]["operations"]
        error_list = []
        for operation in operations:
            challenge_id = operation["challengeId"]
            operation_name = operation["operationName"]
            if operation_name == "complete":
                ret = new_challenge_handler.update_challenge(userId, challenge_id, completed=True)
                #ret = update_progression_batch(challenge_id, userId, complete=True)
                if ret:
                    wallet = mongo.get_data_with_list(login=userId, login_steam=False,
                                                      items={"currency_blood_cells", "currency_iron",
                                                             "currency_ink_cells"})
                    currency_blood_cells = wallet["currency_blood_cells"]
                    currency_iron = wallet["currency_iron"]
                    currency_ink_cells = wallet["currency_ink_cells"]
                    currency_iron = currency_iron + 340
                    currency_ink_cells = currency_ink_cells + 340
                    currency_blood_cells = currency_blood_cells + 340
                    mongo.write_data_with_list(login=userId, login_steam=False,
                                               items_dict={"currency_blood_cells": currency_blood_cells,
                                                           "currency_iron": currency_iron,
                                                           "currency_ink_cells": currency_ink_cells})
                    pass
                else:
                    error_list.append(challenge_id)
            elif operation_name == "save":
                operation_data = operation["operationData"]
                value = operation_data["value"]
                ret = new_challenge_handler.update_challenge(userId, challenge_id, value=value)
                # DEV NOTE: "/Engine/" is a placeholder if SAVE and if HARDCODED
                if ret:
                    pass
                else:
                    error_list.append(challenge_id)
            else:
                logger.graylog_logger(level="error", handler="executeChallengeProgressionOperationBatch",message=f"Unknown operation {operation_name}")
        if error_list:
            logger.graylog_logger(level="error", handler="executeChallengeProgressionOperationBatch", message=f"Error while saving challenges for {userId} with challenge_ids {error_list}")
        return "", 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_executeChallengeProgressionOperationBatch",
                              message=e)


@app.route("/api/v1/inventories", methods=["GET"])
def inventories():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    # This is a Base inventory with every Character unlocked and every Perk LV 2
    base_inventory = [
        {'quantity': 1, 'objectId': '0606F8464D4C7EB70601CC84C50BCAC6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '22C48CEE49DC29EED48A82A7423DCCE6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FF5ADA454579CD95C8536DB944C75F24', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '377368444AFD0D25687CEBA2B721CEA9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4BCE89A640F8687625ABF58B35A734AC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '14CE31244B59876FD5EDCC89F51261C9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '408BB4E642F7DE5488C59B8B0D9E7E59', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '50A1E7644F21463D6C2BADA09CDC5360', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '540C247746391BFD55813DBB9E258AA6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6CF7CB024B2C61996F1888BEA97E611C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '86C70C8D4C5B7CA93417F9BF319FD6F1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9B9218FB4DE925E6C729FA8162FDB505', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AEC0DB8C4EC368F5DAC06A96CEB2D937', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C9DEDB8F4BD6F13359A0359B81F28E77', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D7D7D07B4FB0FABDBF8C3CBE62EB6E96', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D93A7E864CFECE74FDE2D9BA50AB7135', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DC91C3414F22F217BCB30590FAB59A9E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0E262D7A47567BE03A49ABA756FC1482', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '23744B06493AE1220576529C4DB530B1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '272369C042147225E364CFA42947859F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '492232504161420C872A0F82FC16ACDB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4E171BD14FF98ED43A7AFAB57FE55578', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '51E112D1407DC2F33CD6C98B31E1F1BD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5A2DD3F6433AB83A725513B868D240CF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5D230967452FEEE13F1CA780F580E889', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '62AF95414827D3B29B9DFD97D54F1E95', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '69055D534DF27180C4B36CAB4B651054', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C9C6D40A4D6A6A5748D5C0A17763C9C1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F42C5B4148F22D29DA976BA8667964F4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '06BF4EE54025C17B4C548BA36615B37B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '283F2EA44CEE7AE78E097C81B66F1652', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3636FD2240F282F0921FA68E8F88ABBF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3A6C091C47CCD38B0E2086BDD3C2109A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6191DD1B414259E00B1ECDB92F778D36', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8426F8E540BA2F4922856B892E0A7FC1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '981356004D7BD078DC509987E6B51B01', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9900F2F64C656E148EEC5C9BC028B936', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A1C4E2FB4BC74EB560F431B210C5094C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A51608C9465510C0CE78779E0C164C86', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BE76A25F44710E8AD011B2B74ED3F3A9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F552A0AF40D1CFABFE44B6AE09E5C0AA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0FB0413D443180B2812B71ACEE1ED86B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1F688D924FD019AAD7C7F8A5B6580F39', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2920B01748AA9AB4EC6299AD15FF0E6A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2C1400904D1A3B3F22CA068C2ABF2928', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '36C23757408F497712793CBD47421969', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '43916EE24C8F0395C826A2960D23AB6B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5765929B4A8BBD636017188D1DA787EC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5BC76AEF46DE2C17997CB79079576EC5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '89AD14A848DE42DC2A5CAB94BB25FCF9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9B6943CD4DF6CD2FCD94CB89E6F55380', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D4F9F6FA43A8BFD113FCFD9684F6262D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E4D525404770E39E9864A29DC690DB89', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2331ED814F30635500FEDB96A0674A3A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '36CE4DFC412B8FDF255791A609CCBEF4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '426DD9374C6C608710B8B9AFD115476A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '461633744E4F7BFDEB51A8B69718AE83', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5D50CF9C4D2ECB4A094314B62B8D4FC0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '689C9906438BA3B3753FDD8619A72131', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6F6A7923482BBE1183780F8F4B258379', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '895471FA4A8A74AB2FEE16BF35FC9D04', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8B886664468A2878B26813A097F375E5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'ABD448BD42E784491FDE48AD31284348', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BF4B98824C4FF1A0645E059F6FA49B61', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C6D5274E4A50AF3356AF71B0CF0B53AC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '10160BE64538EF4D5D3B4E82D21D9F04', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2822F9B547761DD69A4853920A5A3A67', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '287E08D341A4C1D79E16A086E603A926', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2F32222145A7933E3F1BEC933FA0D986', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '32DABD16440CBC1F37FFC398A995CB16', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3D1CEA184200C624864F1B9B2EA6D6F8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3D5693D941E0CFF7FB4BB4A346775074', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '496CC3BD4E3DD73E70894C9F28D74BDE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '50DBE604449E3B97237B7FB8282DCFB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '50F9173D4A2E6AC649390393AD8A1876', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5A7545B34F4FB2EC39472BBE6680B2EE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5CC40F60479CDB032E2B3D9D2B4B68BA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5F89822342D5E60F474080A36A7E6A5D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '624556DC4373E81D4FFAD8A90D0FECCD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '73D032E24373AEFD053BAC8659626AAB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7A786A464BFC405C04E9B186B49DACF7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7DDD64BD42ACABB1645972ADE5DD8C20', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8251BCB742EE7DD4A860E187B13DD9DE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '840D4D27456FDA5062BCF592726B93F7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8438827D44AA0C807A8C85ABA3A9481B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8A5E53B94D27C821B78CDCB164BD839E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8BBD6D6B46D7EA3BFA362E901C11A0B2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8BD87A0440DAF255AD0D07AE807FF56B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B0192F294B3837DD4F9DC48F4B1C7995', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B245A69F4145075488DD01A477A24385', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BED54888465E38C92F02F194499D8B8A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D62B0CDE478D100230D48C9FD13C456E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D6968E3A4A1FA968F13097B35AF2D61E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D738850D4DC5527A6140CDBBB8006512', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D73CB2D24A0FF4CBB073C4BBE4C5D946', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E34B96F94D82029D83EF6F902DAEDB77', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E578456C4515E0D2291A7FAA99AE6C17', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F20F6E2E4F3162124A476BB9FE07E407', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F501B9E34800BEA6B29CFC87C1584669', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F732FE3845585D24E94AE39BA12D5E71', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F8E2A13648900939B5B086B2D61A6E43', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FD1F569B450C253D3EC750A68A9A177A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F2768C4541C8262EFF4922B372AB7306', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F05493F04CF30636487243B5776882D6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E4892E8A495FFB38F90729A1C97F3AC9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E30FA007473CD2472AE5798B679DA419', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D495BCB543F2D005B559C888E4BF2B3B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CAA84E294F02ECF88B08FB96E481194D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C7A898A44F208F9F85CE75969A98242D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BE1C0D4C4CE0861122BE22B2736D9091', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A858CAF640A824508A028D89AFC44366', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '320652184E1A719DEF1D3C9395EE7344', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5681640F41DF9BEF0659C3A951BFC01B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1258297B4BCBFB39628E22A58C77EA87', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '97501DEF493625107AEDCAAB2ADEDF4B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '60542B19472C7AACEABFAA83D8112ACA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6340FA564B0C4E692AD174BB743607F5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5889E8B1404109B1D4623B9DD2057608', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '04650B23493C386FA87E48947D26D79F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '366DFB0841631FE3A1F4FE9BF814CF2C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '350B26074604529237BF0CB22B60A9B8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '274EB0B34AB39E468BFA878F7E87465B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '105AE7CE41DBBBE92EEBFBB32FDFEC20', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '78C4B6734B7C9DD1D2488EBA8EB5A7E4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '75A9B5A34CD7815B6D77248506897122', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '48C47A4341B0E3E001F3D18537658D40', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '38E5F7F241E2BA1177419BB312FC1ACE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '25BF0927456349471A1C77A852342246', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '20FF1865462FD26B0253A08F18EFAA10', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '19FB62054E644ECDC831E29FC5B9E501', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9FCAAC9143A827E79DC179B762B1E520', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9B34059A4199ACBEE46BB4B0472E7CC3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6A8FA1C845AE1D7576BD87A53F7ED4A4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '04FC953E40A601200FA1C181A0D3C913', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2F3693A4473188D2787CC899A70DC563', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2BD43A50459BD9094DADC49A0F5F2551', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1A09DB19434DA733AAD3D9B5B1929CD4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0EE6E3C04A608FF0CE64A8813A9EBE26', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '168A9C7E4AF1C1D321885ABEF7538DE9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1D86DC084F0C4D3FED2552B08CC2A252', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '33C33E06432AC0DE64158A8A41145D8A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3B0649F041FD918FFBD624B15B64FF4B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '418880784C86E2A81AB395A998B09901', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4754B7494BA24E0272C5DAAD5AC009CE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4AE4801A440EFF8B54760EBFF92B128C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '503AB47B48E0037446EC1197C19A9194', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5DA9F0DE40A95322DC5453A4F85B7B2B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5F747FA544A2274998605E937363B6C4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '69B2207C48098CEF66D2FBB0C0CBF7DA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '71D83BEA40F74032C260DA93B535DF3A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '748671E04848191A65419C8FED546AA2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '75CFE420468721940B8912BBE45092F0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '83FBBC7F491C9C6C61596B858BE9E0B8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '88A823B845E70E80CC4F9BB6E4EAD02B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '92ECE5FC49294EE94DA0D4AC003CA2AF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '95D96ED948ABA024206EF698FEF7B356', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9729860948356C55894620BF8ED4CDCF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '984B33154FE2F069382B0999A1F4BEED', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9A9042614697C385E5744C903F5E19C3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9B2D646948E39CCA5C256DBBCB169543', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9EB999F04DA57E9359D304AA061284D3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AA96AD8F4D4572BC100E06B19164F647', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B8EED46C463FFC70BBC122B9F05FF9F7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BCFB06D543FDAB344CB2E9A2F68EBF40', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C01CD6B543CD1D560D6CAA8C4048AB85', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C90F72FC4D61B1F2FBC73F8A4685EA41', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D670A4624045B40EB7DE4D9F4A1497BE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D81228EB4E6440D7398D6583AF9304D0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D877B29A4EF20A047BEBF69A18B2A1AB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E3B30F55417858D2D6E017B2360B88D6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EF5BBBFD49DEEA174AA5598997FB6B7B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F287ADAA442711947C9BE6B0B3030F93', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F71C636F453DA292ED7AF2A595292462', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0537F9A54016B93E5BE8A6979BAEC91D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '08218CBA4F31403770364F8ABB50DDD3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1F0AC96B47319A47310A4A97D0F44B11', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '25B8F52744CAEB17E599888B5E80162E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2ACA69814FCC99FC5F2EE0B08C4D5E5C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2D391C604941F465AA4EE7800AEF401F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '332697BF4D9CAB645CD7B3ABBB3A0324', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3506BD4A471DF62242C2DDAB46DCBB80', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3C5DD9BB4F684D57D5BA6AB357AFC40B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3E01F8FC4FBBDF78B8D768AC43C7741D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '42E05FC94E6B09CCBB6208BAF94AE98F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '50FB8AA844F1F9DCB0D04790010A5457', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '53E8A0D044F3FA2A808503A702BE1842', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5A8F3E354CBC6F8B5BD015AB89DE031A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5FF316064261F76895ED0EB830E9184B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '75831C73438DA8C3E873339E58FC1674', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7F33795840136A9EBC0186A529E4A82A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '80820F1948FE3E53E6A48296BADC2A9B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '832CDFB74A4C1A77BF4875BABEB31287', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '83C8C4CC4B782FDBB03498800F0CB0B7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8CA68C41427D2758CC8F63AC7D01E8D8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AD1759374CC44614DCC46DBA60A9C670', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B2BC1DD14B33F2FE31AA72842FEC3C2D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BC41691D45E103C2FA81DCA9905AEC9C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C23A3E48469C4630D5CB669B65F86542', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C4F3B1A549C74E05FAE973A524EB2734', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CBE63CAE4215643C4FDE1CBB4DF8B265', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D500FB67476AFA419553BF9F384A9CF2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D538AFA44F9EE94FFAB0348E225F62CB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EAF934964116604C0329FCA56BF27C1E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EC0A479146666CF547C9F5B29CAAD5BD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'ED14BB8240B4AE8124EDA69ECD37AB10', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F329A7724E21169E99739196DFC797D1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FABC2C4E40C5FA74D13C9D9BBDA12C20', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FC3D5C6B4D2547CDA76CE8BA1D536A7D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FEE8A7004DC0DDFE1A22AC9156675E92', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '03B907684E4B8058A274F1A1958A7FB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '047EF3FB48C3BA45374657BEAE90707D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0498C28C4468EC81BA43B585D4D759ED', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '07F69DF04A52519A3B301B923C105277', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '089D250F49D3BF09556CE9BD360A1994', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0BC950834BEA8778AA29D8BAA14728E3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0E8EB65140B51EE188A4819FDF585E09', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0EA4EE824E173A94321092BBD5164050', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '20448CF9452155D51CF3A596AEEA9F93', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '26FD3399444E416AE5BFDA913D2D0FC1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2F12511B412A1B310A55E09CDE252ED7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '36D74C974A5ED5B3FEB1C08D22C7C5FD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '49FD9FAC4873805D1BE812BF907A5F3B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4FDB6DFE4E545F793CEF5780D40B84A6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '51CAE9D747988206193B08BAD648FF96', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '540987164DA1348FF066CC92EC3E748D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '594EA1A64C78A189C2106C95DCAE7030', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '61AA5ED34F4A473099FCDEB11D0ABDA0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '72FF4B494F0257218238C695F072D794', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '75CED6B24CCA9FDA4D976990D0A65172', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7919E64C48E49F575CB7178BE373CFEA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8206DA294E48B55CCF15CEADDC1DE13E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A0138AA648CE0DF4BBDB969A25C32EB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A98210A1445FF0F081DA24BC28BD0D88', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B9FD9CD4489CDBCA483E96AB689B1FCE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C2C46E9047209670A929EBA155D5AC03', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C40EB3E34F9864E4A9BBD2AEDC692224', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C74F3BFB4B1020B9A33BCB86DF5BD142', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CCA0BF8C430D4BFC1EE095914BFF5E4E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CD7D1F824FA432FEA6310B91EA158DB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CDF0CF394DF8ECFB49C2A8AE92BAAA78', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D63DC301472FB3505E0E00BB878404C9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D6FA3760472DD2767D7C6CA90945F0BF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D8222C7B43D329E380496AACB190D183', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EAC46B4C4979624CD3C15B9189D1CC93', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F378019748154C368ABB579594F6CDA7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1A3D862D468B014FA25F0A88DDCA8525', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '21C5A9CD4D61ECAF69320B98C1AD5F76', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2FCC2D2E4CF28ED92EE037976B2C3B82', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '30A3C1AA49EE718D9440E7A50D0CB832', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '326BC4D94285F74B62EEFFA3E45652F8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3785BB3F4E2BD48E9A30098043F0C0A0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3AFC7E854BEA742DD8B844BE3F2FA00B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '42A381F2430D5581EDBD0F8AE66A6380', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '49514CD34903738E75368A90B62BD0CE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4D79F6B34712B0A10F8AA2ACE79DB877', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5DDAC05F4AD79C71B76EA5A61CD078D4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5F1249524EE87F0CA9B143B1D8C0C93B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7D7A6F2D4E7FCB1E1A64D389285AD695', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7E151C2F45B67D737AA62ABFFF5B5199', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8D67A05F46FFA93F13DAC6AEBC4EB618', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '91034CDD45265B562760E8922617B9B4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B39D44DE4A41506524F7A7BF20D69900', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B6D6ACD9480AEC49F4DFBDBDE1D534E6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BC8DB39C4A4173D137B90193C2A460D9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D62016A04A2A00E846EB309753C4AE34', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D79CC57149FC13D3CCD55A921E6B48DF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E29233C54A6009702E235CA973AC356C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'ECA09E174C7D202AC39A4BBDA68E5FFB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F5D3AAFB419D0F14DDA3F6A334F4A6F0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '00CE22624386379A86512A9500B41ABC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '08E1B04246C86826FA5FBE9B8030EB01', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0C6D2A4648B95C2264312783F977F211', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0FA5CBDA402FB9FCC8B56CAE69202061', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2046082F4049FFABD5A933A4559B3AE0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2DBF9B114B82A63940936396CBA68BCD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '305F597C424FDD0A0A6B2BB6CF5CC542', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3C9D2E0A44ED015979667DBA4F080B49', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3D3C4F024308BA7C67306783902EECAB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '47FCA62C449C01963D2293A422A41CF3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4886DDC446B96FEE1255D6A2AB114B0D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5998C1C548AB7BDA80C87295F2764C5D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7037D4804CB9931A4DDF23A35E321775', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7899428947342326CE6B3B83021529E8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7CE5AFBF459102E5728DCDAA6F88C0F1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9281A7AB4EE28B4FB6341886DFD50391', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '97D7970A47CDE0451384D098E7E4A681', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AA00BB584A47234168A63D9F14C4C4E8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B7287C204907B7DDFC7D0EA0B8252E60', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BFC78D3E4DEFDB5C6369A7B0EF5260C9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C215B81F4E42196103ECE98949892499', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DE624DB646B9EEAA7CBDFF9A62D96293', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EB90A75F44EA4D821B385EA00B45E1BE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F055513D48AACBAC280B2AA00A984180', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1D7D54844A373E8A1593E68D29449BC0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2419BFCE4D1EAAC83E0842989764168D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '34B93AFF4487314BFDA9DB96A98A2EE4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '41EBB3A541A9D4F10E5F1F823525FA70', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '55317D914326D128B80FF0890F49DEF4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5F114E9042232BBAF42A328DA24CA0DC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5F1FE83646A31A900DB092B78FB7A5E4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '64993A47498BE7E7B461B6847593961D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6835F1E643D0588CBA2469A8D683E55C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7493289B4C0E2DE6698961A7E24648B6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7FF66ECA49B0A1F16FDE8DAA7F352115', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '889C512941A27F89D080EB9A110681C0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '94AECB834F7899FC2ACE31A5D926B724', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B9774F024DBA47E4ABB0148C7A048B77', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B9EDA06B441115936D7782B428D2E4E3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C22E6E904E21D58FD48040B131A37A86', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CB81ECCF403CC58EF70A05A79CDFB1EC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D0A26483421CB405B5DE8882AF3880A0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D293D67445F4A73238B270BFC352735B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DE5AAA0948FDACB251FE4B8D74A1D1F2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E56118B643396600FB9BB68B9456BCDF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E8055D2644D59134BC6B5C99F0ECBBE0', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E98409444718D31F2426E3B7470EC8F5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FC1B297A4A6F6EE7867485B3AAFC20E7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2690A0F44398C69C52DD888BAF1052CF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '334E917144CB4F07D3A4538E62A0A5E6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '36E43D224F0BF59CB9AEDC959C12AC88', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '386407AF4AABAE4DD467B0BDACC43BCE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '586E501645783071E84AA993A1EAC254', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '614E01E64FB84750E626EFA9DC8E144B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '97E3C57C4A4F305C1244F6B3D9E70D1E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A0A54D22430433E3BA95958E745B6075', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A5413F5F441F471E4EDD618D6CF3879A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BA0AFE1E4B789E380FFF01831EFFF4EE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BBFC928A401AD980745316AE68B8616E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BD37B5154E3FE64FA79F76B83766F4F8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C1A307794F209CD3EA06F788A9952C72', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C8574001477710DFB964919107E749F5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C92B2BE34FF7B665B0B8B7A6F5D10D4E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CA91B3F84D45FFC44986029B5F77CF06', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D280DDA04D5EB4E8317C338DB979A455', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DF733C3844D6574A5A59B8AFA30F9CB1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E6F42CD6478D940657AEAC86A83176BD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EECF881E42C25CC38E0087A5A8D28862', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EF1B789D43B41CFF9E86FCB5E386CE1B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EFD7BA2248692DB48A979192E2187AB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F3E8289F426A68B3C2AD9D9404FDB8BF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F84233134FA798D2958DB9BCE9A4868A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '088298F54D72E0968BF0AB97D96EE2BC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3228707B4880211DBAA779A463AF4401', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '42E7858F4B381C78086D2DBBA21A2265', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4C57A8814E6728324CC3E5B141F9E256', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4C886E474C5A00EEAB07D29286FCD1B7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5C0E2C8C48C032345629789CA6029796', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '661A7F3E460A187260DD51A50FCA2239', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '67059CAD471099DDA98DE19D020F55BA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7EEA14B84BB8E453A006479D71296288', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '932C517242D89178AE68AD9321C71499', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '9736670249461051869F2581EBA62459', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AC483C95413EDE1267B855A4CBE9745C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B6CCC7FB4025BF4289E68F9A69C8A052', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BD5E67DE4CFBBD4A7A06889F782D5B03', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BED70D984E4595F82E0DFA8C5EC570B7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C1D9AADD409C8C031E293582112E75C1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C2C348F84AA173974F9593B0EB065114', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CA4F8ADC49B4F6C1F4303290040DF9DC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CCE33A8046E552A7D9A4E6B9DA9A9C39', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CF8732C744175FA409FBA185982C6C07', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DD6708E941B7F392087653A60FC390AE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E4B12FB94D398B7F289339A42B6988FB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FC27E1D04C3CEE2C5B1D439DCD2A28C7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FD3F459641F187C9E4B2538FE3D237C2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7902D836470BBB49DE9B9D97F17C9DB5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D14477DA4ED69E001DC36ABCEA0B42BC', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '10A8C667458016646E2EFA9452E3141A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7A541DCB4F04DAB2E10FAB84395BB967', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '11035634461C25A5691D2CA41A8DD98D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2FBD62CA46D16FB8923AD58491AA3B7A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'ADD2D777499D30AEC4CEF297F1464B5B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'DC8AD78A440E27BC10A0698E070B5A67', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5A8EECD249F8766AB9E340AA838A0BE7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '7F68BAD343E4840AB693E898E44E8090', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C4B10B1A427F656621CBFA909B6563C3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FA356F204602AE7333F069964D7D4C0A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '206926C247DF099A4A4767BA595E1A7B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '568754AF4288DBC3D112289DB4258377', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6025D0F3480D672CF5FA64A2686D9F6D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E332057B4764F4AB3B2617ACC3BEC03F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '43B9DA8B4F0EBB85FEEBF19AFEF00D36', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '94123783435C622ED2333ABA5DE95BCB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E450C2EC4B17B1E1E713BCB142B6A909', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E7A4686242E54C8FEB195E803B4BDFB2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '50D3005B437066E4C4D99F9397CF1B0B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2BBB9DD842102F0818864F83FDDE8577', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '682EC6AF444E8B15035489B7B59D7026', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EFC6A5BE442C2554DB9D84AC5F2F0F5C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0A9DB5BC418E1EE3F256D59129BB4E5B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '738CFAEB44A48BF6DA5F109C50068BE3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1D8C5DE1493A0FC90E037F9DE8AB698E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '085364AB477B3945124BB18BD875ADF7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '62371A4240C8B4E37EE697BC1E2B1FBF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8412E7AF4072C4FED79F94969178006E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '48072EAA49C83C6F387236955B3C7B6E', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CE9B843E414FBE382247C48F935CC5FA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1054BCA742B538D9EF7C5482B6A94B51', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4F5758F14D7404EB36CEB79D1917F35A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5CBB9D9740F8A4B0CF8A63AF7F336C8F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1B51D59C47F565A20E743BA187B83642', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1945D4B24A31EB6C6CA508A4CDFBB44F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '86711D8347A60ED764BE78A051CD4C11', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '192EC9DD4F40FE3C66F8A2AD84568769', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CA7D61574EB6F0AE1D6D39A4EDD719D7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '2732AE1E44D10CF38EE2BE9A5927AA6F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0B14DB78493FC642908A88AD910F66FA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E414C42947C4DFC2763EDBB5BCC08629', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FC5AC36C4D43405F92A3ED84B2923A24', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '8FB116484CE9929D07267C9E7E7581A9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '364665404243311408F6A0BD4DCE05BD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '1727C5E74C3C7454A6CC0FB1F7562CE2', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '065629E04A181ADD3062169AAFB88F43', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0D96281E4440DF505B9CA8B1457F50D8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '858747E74B7F30A0F6C77888D2D255AF', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B83A141A45FB8D96D48A5185CD607AA3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E4B6A31141FB3AF9271E18882CFC0DB6', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F8240052491F02CD1F1B73854173F0EB', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'FB23E04C4730F3451388DF8CD2FAF31A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '42029CB64E6D0E28CF818ABF164C7DE4', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '307A0B13417737DED675309F8B978AB8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '973C9176404A29F926D13BACB76A2425', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '0FDFC87D45DF769282EA1FA7AB57E409', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3540E3DC4010A6EE61C1CE8002EE4633', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '3D535D304B5E5113CA31D2838C840129', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '792590BE451B239CC0E6838C3B2E0C11', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '472DB7284944C0E569411DBB33C07107', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '656CB0C644C6677C470D21AD0EA8437A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '5691AC1B43E8AC7606D59BACC213FDB1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C55D9EFF46EB08ABDD8467BC23969E53', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '6562B26B48C9C791C82A3EAE344EBEE1', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '90F742AD4BDE1CBF81B4B0BE57271C9B', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'A87672CA4D2BBFF35E273C82F2524278', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'B02BE54A4758C5169593BC9EFF9DA028', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'BBA2090F49BA1F26443400AC8ABD6A7D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '89A14A794CD70E50ADFEB497B89E4381', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '610A3AB34452ED8CD75B36BF033712C7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'D9237F6F4D8D954FAAB9A485885249E5', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '139322874C2271776CB055A310B31107', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C31447C1478648B970D96697EF2DD4C3', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'F7B0756043C628036D038BBED754E89A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '022AC78D48C408C334516A9048A238B9', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '4DE5990D47B51EB2989AD0A52C6A5AE7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'E4F1E5FB490D72F44BD616B5855A2F2C', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'AECFE64B4E7DD00D40EF2BA5CE4468BA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '56B7B6F6473712D0B7A2F992BB2C16CD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '759E44DD469C284175C2D6A1AB0B0FA7', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '234FFD464C55514B6C1E738645993CAA', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C300E3A84E571D549E014B9051A18BE8', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '755D4DFE40DA1512B01E3D8CFF3C8D4D', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '38A4EF8140822E498B2FD196B757F7AD', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'CCA2272D408ED95387F017BED437FF9A', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'EF96A20249884D437B87A6A4BDE81B7F', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': 'C50FFFBF4686613182F45890651797CE', 'lastUpdateAt': 1715019493},
        {'quantity': 1, 'objectId': '606129DC45AB9D16B69E2FA5C99A9835', 'lastUpdateAt': 1715019493}
    ]
    deathgarden_1_inventory = [
        {'quantity': 1, 'objectId': 'FD93572C4CF2DFD134E6D9A90252F665', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'C645C7AC405B3D8AF8E73B946875F0AE', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'DADB36D34727AD788367D58873AB2106', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '428EE16F4F00056E576CC29ED83B8DAB', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '996863814494FF8C7B9531A7478FE762', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'BEF2872E4B3188B43B77EA9DCDFDE0AE', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'C0F44BF0417ACA353D0B8E8A26B1B1AB', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '0EB2781D45D950C6525B8CA308811AA3', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '0FDDDD6A45C0856D0B3EA785B1F508BC', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'D60E21A84EADE0E910DF2FAD7D382699', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'E59F6A1E4513039087919CA078090BFB', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'EF96A20249884D437B87A6A4BDE81B7F', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '2B011E8F46C37F900F8D40A9A73782EB', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '6A7E87AC403EF62B151C27A051B2E373', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'F4B0185D41460D68A0CF7D9A00ACB6E7', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '7474DFFE4A04B58BA12954B430637120', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '29447D464334997ECF872F8B08FDC442', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '2837D67046DAE1E3BE4E749A51BB555B', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'EF8E713B41CA7626D83D39BF05600FA4', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '34918BAF4507ECE322853D8D6DFE81D4', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '755D4DFE40DA1512B01E3D8CFF3C8D4D', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'B35F363447360EC17BE1BD92D827E08B', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '0ADDB41F4216A32D8F1853BAB25D20F2', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'DF5E3FD049902AB5DC1B3C8E22625AAF', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'E501095545F87E64AAFC74A04F1CFF5B', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'F9D4700D47DC559C7CCE11800F3A318A', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '6FF69DEE4FBC9CE82CC2818EE7864EAB', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '03175A2941AB8800F4CAF39ADCDDC663', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '7E2AB46D4BA6F40F03BA768A6F31DB17', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '8968BDBD4AB5F7017A446BB78416EB29', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '97CD4AEA444D6BD2CD218E92B7B12A33', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '098612FC4A3C827849BB55A59C2BC258', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '40E89D554CD74E398E5BAF86369E7C81', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '4302DF13418EC9BE3C8E119F390AACE2', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '865A380D485284B3C5A9409E04C22551', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '3EF7ED3449B8EA4E19BEDFBD100B1DFA', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': '0600201B48B6E1F0B583039E01F8E909', 'lastUpdateAt': 1714521600},
        {'quantity': 1, 'objectId': 'C300E3A84E571D549E014B9051A18BE8', 'lastUpdateAt': 1714521600}
    ]

    try:
        page = request.args.get('page', default=0, type=int)
        limit = request.args.get('limit', default=500, type=int)
        # This should be added some day...
        items = mongo.get_data_with_list(login=userid, login_steam=False, items={"inventory"})
        for item in items["inventory"]:
            base_inventory.append({"quantity": 1, "objectId": item, "lastUpdateAt": 1714521600})

        hasPlayedDeathGarden1 = mongo.get_data_with_list(login=userid, login_steam=False, items={"hasPlayedDeathGarden1"})["hasPlayedDeathGarden1"]
        if hasPlayedDeathGarden1:
            for item in deathgarden_1_inventory:
                base_inventory.append(item)

        if page == 0:
            return jsonify({
                "code": 200,
                "message": "OK",
                "data": {
                    "playerId": "userid",
                    "inventory": base_inventory,
                }
            })
        elif page == 1:
            return jsonify({"Code": 200, "Message": "OK", "Data": {"PlayerId": userid, "Inventory": [
                {"ObjectId": "C16725414A4B16B9AD557C9EE865D113", "Quantity": 1, "LastUpdateAt": 1687377305}
            ], "NextPage": 0}})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="inventories", message=e)


# idk if this works
# i dont remember this endpoint be called in live. So probably OG DG/0.3.0
@app.route("/api/v1/players/me/splinteredstates/ProgressionGroups", methods=["GET"])
def progression_groups():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
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
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        ban_data = mongo.get_data_with_list(login=userid, login_steam=False,
                                            items={"is_banned", "ban_reason", "ban_start", "ban_expire"})
        if ban_data is None:
            return jsonify({"status": "error"})
        elif ban_data["is_banned"]:
            return jsonify({"IsBanned": ban_data["is_banned"], "BanInfo": {"BanPeriod": 10,
                                                                           "BanReason": ban_data["ban_reason"],
                                                                           "BanStart": ban_data["ban_start"],
                                                                           "BanEnd": ban_data["ban_expire"],
                                                                           "Confirmed": False, "Pending": False}})
        elif not ban_data["is_banned"]:
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
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

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
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        currencies = mongo.get_data_with_list(login=userid, login_steam=False,
                                              items={"currency_blood_cells", "currency_iron", "currency_ink_cells"})
        # PROGRESSION_CURRENCY and HARD_CURRENCY are from OG DG.
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
    except TypeError:
        return jsonify({"status": "error"})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# Does not work. Old DG endpoint. Not needed.
@app.route("/api/v1/wallet/currencies/PROGRESSION_CURRENCY", methods=["GET"])
def wallet_currencies_progression():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        return jsonify([{"Currency": 1, "Amount": 10}, {"Currency": 2, "Amount": 10}, {"Currency": 3, "Amount": 10}])
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="currencies", message=e)


# OG Endpoint. The game now uses Challenges for Achievements
@app.route("/api/v1/players/me/splinteredstates/TheExit_Achievements", methods=["GET"])
def achievements_get():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        # I don't know how this fixes the console error but if it works for now idc...
        return jsonify({"UserId": userid,
                        "StateName": "Fstring",
                        "Segment": "FString",
                        "ObjectId": "",
                        "Version": 1,
                        "SchemaVersion": 1,
                        "Data": [
                            {
                                "ObjectId": "EFAB89E6465D1163D62A07B11048F2B6",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "2CAEBB354D506D7C43B941BC1DA775A0",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "E51981B946BEE3D45C5C41B2FCFF310B",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "AAD05B9D46471DC811BBE0BA91916AB7",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            },
                            {
                                "ObjectId": "BA2D4A5445CB70276A8F5D9E1AFCE080",
                                "Version": 11111111,
                                "SchemaVersion": 11111111,
                                "Data":
                                    {
                                        "Key": "Value"
                                    }
                            }
                        ]})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="Achievment_handler", message=e)


@app.route("/api/v1/messages/count", methods=["GET"])
def messages_count():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        flag = sanitize_input(request.args.get('flag'))
        if flag != "NEW":
            logger.graylog_logger(level="debug", handler="messages_count", message=f"New message Count Flag {flag}")
        unread_message_ids = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
        if unread_message_ids["unread_msg_ids"] == "" or unread_message_ids is None:
            return jsonify({"Count": 0})
        else:
            length = len(unread_message_ids["unread_msg_ids"])
            return jsonify({"Count": length})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_count", message=e)


@app.route("/api/v1/messages/list", methods=["GET", "DELETE"])
def messages_list():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        if request.method == "GET":
            limit = int(request.args.get("limit", 500))
            page = int(request.args.get("page", 1))

            unread_message_ids = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
            ids = []
            for items in unread_message_ids.get("unread_msg_ids", []):
                ids.append(str(items))

            json_file_path = os.path.join(app.root_path, "json", "placeholders", "messages.json")
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)

            messages = []
            for message_id in ids:
                messages.extend(data.get(message_id, []))

            total_messages = len(messages)

            if total_messages <= limit * page:
                pages = 0
            else:
                pages = ceil(total_messages / limit) - page

            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            messages_page = messages[start_idx:end_idx]

            return jsonify({"messages": messages_page, "NetPage": pages})

        elif request.method == "DELETE":
            return jsonify(""), 204
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_list", message=str(e))

    return jsonify({"messages": [], "NetPage": 0})


@app.route("/api/v1/messages/v2/markAs", methods=["POST"])
def messages_mark_as():
    try:
        check_for_game_client("strict")
        session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
        userid = session_manager.get_user_id(session_cookie)
        data = request.get_json()
        message_list = data["messageList"]
        if not message_list:
            mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"unread_msg_ids": ""})
            return jsonify({"List": [{"Received": get_time(), "Success": True, "RecipientId": userid}]})
        if message_list[0]["recipientId"] == "3":
            # Moderation MSG -> Do not del (Request by miraak)
            return jsonify({"List": [{"Received": get_time(), "Success": True, "RecipientId": userid}]})
        message_id = message_list[0]["recipientId"]
        unread_messages = mongo.get_data_with_list(login=userid, login_steam=False, items={"unread_msg_ids"})
        unread_messages = unread_messages["unread_msg_ids"].split(",")
        unread_messages.remove(message_id)
        unread_messages = ",".join(unread_messages)
        data = {"unread_msg_ids": unread_messages}
        mongo.write_data_with_list(login=userid, login_steam=False, items_dict=data)
        current_timestamp, expiration_timestamp = get_time()
        return jsonify({"List": [{"Received": current_timestamp, "Success": True, "RecipientId": userid}]})
    except TimeoutError:
        return jsonify({"status": "Timeout error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="messages_mark_as", message=e)
        return jsonify({"status": "API error"})


@app.route("/moderation/check/chat", methods=["POST"])
def moderation_check_chat():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)

    try:
        # Request: FApiHttpCheckChatRequest
        data = request.get_json()
        userid = sanitize_input(data["userId"])
        language = sanitize_input(data["language"])
        message = sanitize_input(data["message"])
        return jsonify({"status": "success", "result": "OK"})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="moderation_check_chat", message=e)


@app.route("/api/v1/extensions/progression/initOrGetGroups", methods=["POST"])
def extension_progression_init_or_get_groups():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        request_data = request.get_json()
        data = get_init_or_get_groups(userid, request_data)
        return jsonify(data)

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_initOrGetGroups", message=e)


@app.route("/api/v1/extensions/progression/updateMetadataGroup", methods=["POST"])
def update_metadata_group():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        data = request.get_json()
        object_id = data["data"]["objectId"]
        version = data["data"]["version"]
        metadata = data["data"]["metadata"]
        if dev_env == "false":
            try:
                metadata["pickedChallenges"] = []
            except KeyError:
                pass
        try:
            reason = data["data"]["reason"]
        except KeyError:
            reason = "SetLastPlayedCharacterId"

        if reason == "SetLastPlayedCharacterId" or reason == "SetLastPlayedFaction":

            last_played_faction = metadata["lastPlayedFaction"]
            last_played_runner_id = metadata["lastPlayedRunnerId"]["tagName"]
            last_played_hunter_id = metadata["lastPlayedHunterId"]["tagName"]
            should_play_without_contextual_help = metadata["shouldPlayWithoutContextualHelp"]
            try:
                has_played_death_garden_1 = metadata["hasPlayedDeathGarden1"]
            except KeyError:
                # old version of game
                has_played_death_garden_1 = False
            mongo.write_data_with_list(login=userid, login_steam=False,
                                       items_dict={"last_played_faction": last_played_faction,
                                                   "last_hunter": last_played_hunter_id,
                                                   "last_runner": last_played_runner_id,
                                                   "hasPlayedDeathGarden1": has_played_death_garden_1,
                                                   "tutorial_completed": should_play_without_contextual_help})
        elif reason == "OnCloseLoadoout" or reason == "Character dirty":
            # Write data to DB
            character_id = metadata["characterId"]
            prestige_level = metadata["prestigeLevel"]
            equipment = metadata["equipment"]
            equippedPerks = metadata["equippedPerks"]
            equippedPowers = metadata["equippedPowers"]
            equippedWeapons = metadata["equippedWeapons"]
            equippedBonuses = metadata["equippedBonuses"]
            equippedConsumables = metadata["equippedConsumables"]
            pickedChallenges = metadata["pickedChallenges"]
            object_data = mongo.get_data_with_list(login=userid, login_steam=False, items={object_id})

            database_dict = {object_id: {"prestige": prestige_level,
                                         "experience": object_data[object_id]["experience"],
                                         "Equipment": equipment,
                                         "EquippedPerks": equippedPerks,
                                         "EquippedPowers": equippedPowers,
                                         "EquippedWeapons": equippedWeapons,
                                         "EquippedBonuses": equippedBonuses,
                                         "pickedChallenges": pickedChallenges,
                                         "equippedConsumables": equippedConsumables,
                                         "characterId": character_id}}

            mongo.write_data_with_list(login=userid, login_steam=False, items_dict=database_dict)

        elif reason == "OnRequestCharacterOverrideEvent":
            try:
                new_challenge_handler.get_challenge_by_id()
                get_challenge_ids_from_inventory(userid)
            except Exception as e:
                logger.graylog_logger(level="error", handler="updateMetadataGroup", message=e)
            character_id = metadata["characterId"]
            prestige_level = metadata["prestigeLevel"]
            equipment = metadata["equipment"]
            equippedPerks = metadata["equippedPerks"]
            equippedPowers = metadata["equippedPowers"]
            equippedWeapons = metadata["equippedWeapons"]
            equippedBonuses = metadata["equippedBonuses"]
            equippedConsumables = metadata["equippedConsumables"]
            pickedChallenges = metadata["pickedChallenges"]
            object_data = mongo.get_data_with_list(login=userid, login_steam=False, items={object_id})

            database_dict = {object_id: {"prestige": prestige_level,
                                         "experience": object_data[object_id]["experience"],
                                         "Equipment": equipment,
                                         "EquippedPerks": equippedPerks,
                                         "EquippedPowers": equippedPowers,
                                         "EquippedWeapons": equippedWeapons,
                                         "EquippedBonuses": equippedBonuses,
                                         "pickedChallenges": pickedChallenges,
                                         "equippedConsumables": equippedConsumables,
                                         "characterId": character_id}}

            mongo.write_data_with_list(login=userid, login_steam=False, items_dict=database_dict)

        else:
            logger.graylog_logger(level="error", handler="updateMetadataGroup", message=f"New reason: {reason}")
        get_challenge_ids_from_inventory(userid)
        return jsonify({"userId": userid,
                        "stateName": "MetadataGroups",
                        "objectId": "PlayerMetadata",
                        "version": 343,
                        "schemaVersion": 1,
                        "data": data["data"]})

    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_updateMetadataGroup",
                              message=f"Json: {request.get_json()}")
        logger.graylog_logger(level="error", handler="logging_updateMetadataGroup", message=e)


@app.route("/api/v1/extensions/inventory/unlockSpecialItems", methods=["POST"])
def inventory_unlock_special_items():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    data = request.get_json()["data"]["additionalSteamAppIds"]

    unlocked_items = []

    origin_sets_artbook_items = ["34918BAF4507ECE322853D8D6DFE81D4", "4302DF13418EC9BE3C8E119F390AACE2",
                                 "3EF7ED3449B8EA4E19BEDFBD100B1DFA", "40E89D554CD74E398E5BAF86369E7C81",
                                 "C645C7AC405B3D8AF8E73B946875F0AE", "6A7E87AC403EF62B151C27A051B2E373",
                                 "29447D464334997ECF872F8B08FDC442", "F4B0185D41460D68A0CF7D9A00ACB6E7"]
    dbd_items = ["4EDACCF844B8025FD89C7BAB6B0005A2", "9F54DE7A4E15935B503850A127B0A2A4"]
    terminator_set_items = ["EADE3240481E7372624FF2B186ADE4D8", "ED13D15E4439C1C19281D2AFDD4C5B96",
                            "5AC2450640153C86DF57FA84500DA45C", "361D68284314B8A0A9432D913C93C9C0",
                            "B42F8BA04A4294BAF95A4090E62F66BC", "1B00252A45A9206224ECE5816C99A2A3"]
    alienware_outfit_items = ["ADC2570E4BD4D9AD5FAB21B974B807EC", "D4D6E33D42EE0DDDA24DA983C70209EC",
                              "EAF477EC4CE75EACAE8E4ABE22AD8E4D", "996F45A64E6E2E7B2B72B9BABA86F86D"]
    hearts_and_minds_items = ["70A09B4348F9DA5B1EEF0786DB1911AC", "221B6B19499A30944F8F4A969EB2B83D"]

    user_inventory = mongo.get_data_with_list(login=userid, login_steam=False, items={"inventory"})

    writen_sets = mongo.get_data_with_list(login=userid, login_steam=False, items={"unlocked_special_item_ids"})["unlocked_special_item_ids"]
    if 872770 in data and 872770 not in writen_sets:
        unlocked_items.extend(origin_sets_artbook_items)
        writen_sets.append(872770)
    if 381210 in data and 381210 not in writen_sets:
        unlocked_items.extend(dbd_items)
        writen_sets.append(381210)
    if 1024660 in data and 1024660 not in writen_sets:
        unlocked_items.extend(terminator_set_items)
        writen_sets.append(1024660)
    if 1083130 in data and 1083130 not in writen_sets:
        unlocked_items.extend(alienware_outfit_items)
        writen_sets.append(1083130)
    if 920440 in data and 920440 not in writen_sets:
        unlocked_items.extend(hearts_and_minds_items)
        writen_sets.append(920440)
    for appid in data:
        if appid not in [872770, 381210, 1024660, 1083130, 920440]:
            logger.graylog_logger(level="error", handler="unknown_unlockSpecialItems",
                                  message=f"Unknown appid {appid} for user {userid}")

    for item in unlocked_items:
        if item not in user_inventory["inventory"]:
            user_inventory["inventory"].append(item)

    mongo.write_data_with_list(login=userid, login_steam=False, items_dict=user_inventory)
    if len(writen_sets) != 0:
        mongo.write_data_with_list(login=userid, login_steam=False, items_dict={"unlocked_special_item_ids": writen_sets})

    try:
        return jsonify({"unlockedItems": unlocked_items})
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="unknown_unlockSpecialItems", message=e)


@app.route("/api/v1/extensions/progression/resetCharacterProgressionForPrestige", methods=["POST"])
def reset_prestige():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    userid = session_manager.get_user_id(session_cookie)
    try:
        data = request.get_json()
        character_id = data["data"]["characterId"]
        logger.graylog_logger(level="info", handler="resetCharacterProgressionForPrestige", message=data)
        # This has not been implemented yet
        return jsonify({
            "IsCharacterItemsReset": False,
            "IsCharacterChallengesReset": False,
            "IsCharacterExperienceReset": False,
            "PrestigeLevel": 1,
            "Rewards": [
                {
                    "ItemRewards": [],
                    "CurrencyRewards": [
                        {
                            "Currency": "CurrencyA",
                            "Amount": 100
                        }
                    ],
                    "Costs": [
                        {
                            "Currency": "CurrencyA",
                            "Amount": 100
                        }
                    ]
                }
            ]
        })
        # ItemRewards: UCatalogItemAsset ARRAY
    except TimeoutError:
        return jsonify({"status": "error"})
    except Exception as e:
        logger.graylog_logger(level="error", handler="resetCharacterProgressionForPrestige", message=e)


@app.route("/api/v1/extensions/challenges/getChallengeProgressionBatch", methods=["POST"])
def challenges_get_challenge_progression_batch():
    check_for_game_client("strict")
    session_cookie = sanitize_input(request.cookies.get("bhvrSession"))
    user_id = session_manager.get_user_id(session_cookie)

    # Disabled because challenges still dont work and the new backend has it fixed already.
    if dev_env == "false":
        return jsonify({"status": "error"})

    try:
        data = request.get_json()
        challenge_ids = data["data"]["challengeIds"]
        challenge_list = []
        userid = data["data"]["userId"]

        #moved this call to outside get_progression_batch to reduce the amount of database calls
        #change array to dict for quicker element access
        #for challenge in db_challenge:
        #    #We do not want timestamp in our key otherwise duplicate weekly/daily challenges are created
        #    db_challenge_dict[challenge["challengeId"].split(":")[0]] = challenge

        for challenge in challenge_ids:
            challenge_data = None
            if ":" in challenge:
                challenge = challenge.split(":")[0]
            challenge_data = new_challenge_handler.get_progression_batch(challenge, userid)


            if challenge_data:
                challenge_list.append(challenge_data)
            else:
                logger.graylog_logger(level="error", handler="logging_missing_challenge",
                                      message=f"Unknown challenge id {challenge}")

        response = {"progressionBatch": challenge_list}
        return jsonify(response)
        # return jsonify({"ProgressionBatch": challenge_list})
    except TimeoutError:
        return jsonify({"status": "error"})

    except Exception as e:
        logger.graylog_logger(level="error", handler="logging_getChallengeProgressionBatch", message=e)
